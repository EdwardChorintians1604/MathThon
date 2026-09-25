from flask import Blueprint, request, jsonify, current_app, session, redirect, url_for
import json
import os
from datetime import datetime
import uuid
from ..db.database_mysql import get_db_connection, close_db_connection
from ..security_for_web import user_required
from ..ai.chat_api import chat_ai_logic

ai_bp = Blueprint("ai_bp", __name__, url_prefix="/api/ai")

ARCHIVE_PATH = os.path.join(os.path.dirname(__file__), '../../ai_conversation_archive.json')

@ai_bp.route('/save_conversation', methods=['POST'])
@user_required
def save_conversation():
    user_id = session.get('user_id')
    req = request.get_json(silent=True) or {}
    title = (req.get('title') or '').strip()
    messages = req.get('messages') or []
    
    if not title or not messages:
        return jsonify({'error': 'Judul dan pesan wajib diisi.'}), 400

    conv_id = str(uuid.uuid4())
    conn = None
    cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()
        
        # Insert into conversations
        cursor.execute(
            "INSERT INTO conversations (id, user_id, title) VALUES (%s, %s, %s)",
            (conv_id, user_id, title)
        )
        
        # Insert messages
        for msg_text in messages:
            # Parse role from "You : ..." or "AI : ..."
            if msg_text.startswith("You : "):
                role = "user"
                content = msg_text.replace("You : ", "", 1)
            elif msg_text.startswith("AI : "):
                role = "assistant"
                content = msg_text.replace("AI : ", "", 1)
            else:
                role = "user" # Fallback
                content = msg_text
                
            cursor.execute(
                "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                (conv_id, role, content)
            )
            
        conn.commit()
        return jsonify({'success': True, 'id': conv_id}), 200
    except Exception as e:
        if conn: conn.rollback()
        current_app.logger.error(f"Error saving conversation: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)

@ai_bp.route('/update_conversation/<conv_id>', methods=['PUT'])
@user_required
def update_conversation(conv_id):
    user_id = session.get('user_id')
    req = request.get_json(silent=True) or {}
    title = (req.get('title') or '').strip()
    messages = req.get('messages') or []
    
    conn = None
    cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()
        
        # Verify ownership
        cursor.execute("SELECT id FROM conversations WHERE id = %s AND user_id = %s", (conv_id, user_id))
        if not cursor.fetchone():
            return jsonify({'error': 'Percakapan tidak ditemukan atau bukan milik Anda.'}), 404

        # Update title
        cursor.execute("UPDATE conversations SET title = %s WHERE id = %s", (title, conv_id))
        
        # Replace messages
        cursor.execute("DELETE FROM chat_messages WHERE conversation_id = %s", (conv_id,))
        for msg_text in messages:
            if msg_text.startswith("You : "):
                role = "user"
                content = msg_text.replace("You : ", "", 1)
            elif msg_text.startswith("AI : "):
                role = "assistant"
                content = msg_text.replace("AI : ", "", 1)
            else:
                role = "user"
                content = msg_text
                
            cursor.execute(
                "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                (conv_id, role, content)
            )
            
        conn.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)

@ai_bp.route('/delete_conversation/<conv_id>', methods=['DELETE'])
@user_required
def delete_conversation(conv_id):
    user_id = session.get('user_id')
    conn = None
    cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM conversations WHERE id = %s AND user_id = %s", (conv_id, user_id))
        conn.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)

@ai_bp.route('/conversation_archive', methods=['GET'])
@ai_bp.route('/load_conversation', methods=['GET'])
@user_required
def conversation_archive():
    user_id = session.get('user_id')
    conn = None
    cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, title, created_at as timestamp FROM conversations WHERE user_id = %s ORDER BY created_at DESC",
            (user_id,)
        )
        rows = cursor.fetchall()
        for row in rows:
            if row['timestamp']:
                row['timestamp'] = row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)

@ai_bp.route('/conversation/<conv_id>', methods=['GET'])
@user_required
def get_conversation(conv_id):
    user_id = session.get('user_id')
    conn = None
    cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, title, created_at as timestamp FROM conversations WHERE id = %s AND user_id = %s",
            (conv_id, user_id)
        )
        conv = cursor.fetchone()
        if not conv:
            return jsonify({'error': 'Percakapan tidak ditemukan.'}), 404
        
        if conv['timestamp']:
            conv['timestamp'] = conv['timestamp'].strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute(
            "SELECT role, content FROM chat_messages WHERE conversation_id = %s ORDER BY id ASC",
            (conv_id,)
        )
        messages = cursor.fetchall()
        
        # Format back to "You : ..." and "AI : ..." for frontend compatibility
        formatted_messages = []
        for m in messages:
            prefix = "You : " if m['role'] == 'user' else "AI : "
            formatted_messages.append(prefix + m['content'])
            
        conv['messages'] = formatted_messages
        return jsonify(conv), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)

@ai_bp.route('/migrate_from_json', methods=['POST'])
@user_required
def migrate_from_json():
    user_id = session.get('user_id')
    if not os.path.exists(ARCHIVE_PATH):
        return jsonify({'message': 'Tidak ada file arsip JSON untuk dimigrasi.'}), 200
        
    try:
        with open(ARCHIVE_PATH, 'r', encoding='utf-8') as f:
            archive = json.load(f)
    except Exception as e:
        return jsonify({'error': f'Gagal membaca JSON: {e}'}), 500
        
    if not archive:
        return jsonify({'message': 'Arsip JSON kosong.'}), 200

    conn = None
    cursor = None
    count = 0
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()
        
        for item in archive:
            # Check if already exists (using ID or title+timestamp)
            item_id = item.get('id')
            title = item.get('title', 'Percakapan Migrasi')
            timestamp_str = item.get('timestamp')
            messages = item.get('messages', [])
            
            # For migration, we might want a new UUID or use existing if it's a UUID
            try:
                uuid.UUID(item_id)
                new_id = item_id
            except:
                new_id = str(uuid.uuid4())

            # Skip if already in DB
            cursor.execute("SELECT id FROM conversations WHERE id = %s", (new_id,))
            if cursor.fetchone():
                continue
                
            cursor.execute(
                "INSERT INTO conversations (id, user_id, title, created_at) VALUES (%s, %s, %s, %s)",
                (new_id, user_id, title, timestamp_str)
            )
            
            for msg_text in messages:
                if msg_text.startswith("You : "):
                    role = "user"
                    content = msg_text.replace("You : ", "", 1)
                elif msg_text.startswith("AI : "):
                    role = "assistant"
                    content = msg_text.replace("AI : ", "", 1)
                else:
                    role = "user"
                    content = msg_text
                    
                cursor.execute(
                    "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                    (new_id, role, content)
                )
            count += 1
            
        conn.commit()
        return jsonify({'message': f'Berhasil memigrasi {count} percakapan.', 'migrated_count': count}), 200
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)
@ai_bp.route('/chat', methods=['GET', 'POST'])
@user_required
def chat_route():
    """Chat endpoint that handles AI conversation requests."""
    if request.method == 'GET':
        # Redirect manual access to the UI page
        return redirect(url_for('user.ai_feature'))
    
    req = request.get_json(silent=True) or {}
    # chat_ai_logic expects data and returns a dict with 'response' or 'error'
    result = chat_ai_logic(req)
    if 'response' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500
