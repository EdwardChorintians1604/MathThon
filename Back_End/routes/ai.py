from flask import Blueprint, request, jsonify, current_app, session, redirect, url_for
import json
import os
import uuid
from datetime import datetime
from ..db.database_mysql import get_db_connection, close_db_connection
from .security_for_web import user_required
from ..ai.chat_api import chat

ai_bp = Blueprint("ai", __name__)

ARCHIVE_PATH = os.path.join(os.path.dirname(__file__), '../../ai_conversation_archive.json')


# ──────────────────────────────────────────────────────────────
# HELPER: parse messages dari berbagai format frontend
# ──────────────────────────────────────────────────────────────

def _parse_messages(messages: list) -> list:
    """
    Menerima messages dalam format lama (string "You : ..." / "AI : ...") 
    maupun format baru (dict {role, content}), 
    dan mengembalikan list of dict {role, content}.
    """
    parsed = []
    for msg in messages:
        if isinstance(msg, dict) and 'role' in msg and 'content' in msg:
            # Format baru: {role: 'user'|'assistant', content: '...'}
            role = msg['role']
            content = msg['content']
        elif isinstance(msg, str):
            # Format lama: "You : ..." atau "AI : ..."
            if msg.startswith("You : "):
                role = "user"
                content = msg[6:]
            elif msg.startswith("AI : "):
                role = "assistant"
                content = msg[5:]
            else:
                role = "user"
                content = msg
        else:
            continue  # Skip format tidak dikenal

        parsed.append({'role': role, 'content': content})
    return parsed


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/chat  (GET & POST)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/chat', methods=['GET', 'POST'])
@user_required
def chat_endpoint():
    """Main chat endpoint - memanggil logika chat AI."""
    if request.method == 'GET':
        return redirect(url_for('user.ai_feature'))
    return chat()


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/conversation_archive  (GET)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/conversation_archive', methods=['GET'])
@ai_bp.route('/load_conversation', methods=['GET'])
@user_required
def conversation_archive():
    """Mengembalikan daftar percakapan milik user yang sedang login."""
    user_id = session.get('user_id')
    conn = cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT
                c.id,
                c.title,
                COALESCE(c.is_pinned, 0) as is_pinned,
                c.created_at as timestamp,
                (
                    SELECT cm.content
                    FROM chat_messages cm
                    WHERE cm.conversation_id = c.id
                    ORDER BY cm.id DESC
                    LIMIT 1
                ) as preview
            FROM conversations c
            WHERE c.user_id = %s
            ORDER BY COALESCE(c.is_pinned, 0) DESC, c.created_at DESC
            """,
            (user_id,)
        )
        rows = cursor.fetchall()
        for row in rows:
            row['is_pinned'] = bool(row.get('is_pinned', False))
            if row.get('timestamp'):
                row['timestamp'] = row['timestamp'].strftime('%Y-%m-%dT%H:%M:%S')
        return jsonify(rows), 200
    except Exception as e:
        current_app.logger.error(f"[AI] conversation_archive error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/conversation/<conv_id>  (GET)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/conversation/<conv_id>', methods=['GET'])
@user_required
def get_conversation(conv_id):
    """Mengambil detail percakapan beserta pesan-pesannya."""
    user_id = session.get('user_id')
    conn = cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor(dictionary=True)

        # Ambil header percakapan, pastikan milik user
        cursor.execute(
            "SELECT id, title, COALESCE(is_pinned, 0) as is_pinned, created_at as timestamp "
            "FROM conversations WHERE id = %s AND user_id = %s",
            (conv_id, user_id)
        )
        conv = cursor.fetchone()
        if not conv:
            return jsonify({'error': 'Percakapan tidak ditemukan.'}), 404

        conv['is_pinned'] = bool(conv.get('is_pinned', False))
        if conv.get('timestamp'):
            conv['timestamp'] = conv['timestamp'].strftime('%Y-%m-%dT%H:%M:%S')

        # Ambil pesan
        cursor.execute(
            "SELECT role, content FROM chat_messages "
            "WHERE conversation_id = %s ORDER BY id ASC",
            (conv_id,)
        )
        # Kembalikan format baru {role, content} yang dimengerti frontend
        conv['messages'] = cursor.fetchall()
        return jsonify(conv), 200

    except Exception as e:
        current_app.logger.error(f"[AI] get_conversation error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/pin_conversation/<conv_id>  (PUT / POST)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/pin_conversation/<conv_id>', methods=['PUT', 'POST'])
@user_required
def pin_conversation(conv_id):
    """Toggle atau atur status is_pinned percakapan."""
    user_id = session.get('user_id')
    req = request.get_json(silent=True) or {}
    conn = cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, COALESCE(is_pinned, 0) as is_pinned FROM conversations WHERE id = %s AND user_id = %s",
            (conv_id, user_id)
        )
        conv = cursor.fetchone()
        if not conv:
            return jsonify({'error': 'Percakapan tidak ditemukan atau bukan milik Anda.'}), 404

        new_pinned = req.get('is_pinned')
        if new_pinned is None:
            new_pinned = not bool(conv['is_pinned'])
        else:
            new_pinned = bool(new_pinned)

        cursor.execute(
            "UPDATE conversations SET is_pinned = %s WHERE id = %s",
            (1 if new_pinned else 0, conv_id)
        )
        conn.commit()
        return jsonify({'success': True, 'is_pinned': new_pinned}), 200

    except Exception as e:
        if conn: conn.rollback()
        current_app.logger.error(f"[AI] pin_conversation error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/save_conversation  (POST)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/save_conversation', methods=['POST'])
@user_required
def save_conversation():
    """Menyimpan percakapan baru ke database."""
    user_id = session.get('user_id')
    req = request.get_json(silent=True) or {}
    title = (req.get('title') or '').strip() or 'Chat Baru'
    is_pinned = 1 if req.get('is_pinned') else 0
    messages = _parse_messages(req.get('messages') or [])

    if not messages:
        return jsonify({'error': 'Pesan tidak boleh kosong.'}), 400

    conv_id = str(uuid.uuid4())
    conn = cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO conversations (id, user_id, title, is_pinned) VALUES (%s, %s, %s, %s)",
            (conv_id, user_id, title, is_pinned)
        )

        for msg in messages:
            cursor.execute(
                "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                (conv_id, msg['role'], msg['content'])
            )

        conn.commit()
        return jsonify({'success': True, 'id': conv_id, 'is_pinned': bool(is_pinned)}), 200

    except Exception as e:
        if conn: conn.rollback()
        current_app.logger.error(f"[AI] save_conversation error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/update_conversation/<conv_id>  (PUT)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/update_conversation/<conv_id>', methods=['PUT'])
@user_required
def update_conversation(conv_id):
    """Memperbarui judul, status pin, dan pesan percakapan yang sudah ada."""
    user_id = session.get('user_id')
    req = request.get_json(silent=True) or {}
    title = (req.get('title') or '').strip() or 'Chat Baru'
    is_pinned = req.get('is_pinned')
    messages = _parse_messages(req.get('messages') or [])

    conn = cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()

        # Verifikasi kepemilikan
        cursor.execute(
            "SELECT id FROM conversations WHERE id = %s AND user_id = %s",
            (conv_id, user_id)
        )
        if not cursor.fetchone():
            return jsonify({'error': 'Percakapan tidak ditemukan atau bukan milik Anda.'}), 404

        if is_pinned is not None:
            cursor.execute(
                "UPDATE conversations SET title = %s, is_pinned = %s WHERE id = %s",
                (title, 1 if is_pinned else 0, conv_id)
            )
        else:
            cursor.execute(
                "UPDATE conversations SET title = %s WHERE id = %s",
                (title, conv_id)
            )

        # Hapus pesan lama dan masukkan yang baru
        cursor.execute("DELETE FROM chat_messages WHERE conversation_id = %s", (conv_id,))
        for msg in messages:
            cursor.execute(
                "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                (conv_id, msg['role'], msg['content'])
            )

        conn.commit()
        return jsonify({'success': True}), 200

    except Exception as e:
        if conn: conn.rollback()
        current_app.logger.error(f"[AI] update_conversation error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/delete_conversation/<conv_id>  (DELETE)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/delete_conversation/<conv_id>', methods=['DELETE'])
@user_required
def delete_conversation(conv_id):
    """Menghapus percakapan beserta semua pesannya."""
    user_id = session.get('user_id')
    conn = cursor = None
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM conversations WHERE id = %s AND user_id = %s",
            (conv_id, user_id)
        )
        conn.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        current_app.logger.error(f"[AI] delete_conversation error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)


# ──────────────────────────────────────────────────────────────
# ENDPOINT: /api/ai/migrate_from_json  (POST)
# ──────────────────────────────────────────────────────────────

@ai_bp.route('/migrate_from_json', methods=['POST'])
@user_required
def migrate_from_json():
    """Migrasi percakapan lama dari file JSON ke database MySQL."""
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

    conn = cursor = None
    count = 0
    try:
        conn = get_db_connection(current_app)
        cursor = conn.cursor()

        for item in archive:
            item_id = item.get('id')
            title = item.get('title', 'Percakapan Migrasi')
            timestamp_str = item.get('timestamp')
            messages = _parse_messages(item.get('messages', []))

            # Gunakan ID yang ada jika valid UUID, atau buat baru
            new_id = str(uuid.uuid4())
            if item_id:
                try:
                    uuid.UUID(str(item_id))
                    new_id = str(item_id)
                except ValueError:
                    pass

            # Lewati jika ID sudah ada di DB
            cursor.execute("SELECT id FROM conversations WHERE id = %s", (new_id,))
            if cursor.fetchone():
                continue

            cursor.execute(
                "INSERT INTO conversations (id, user_id, title, created_at) VALUES (%s, %s, %s, %s)",
                (new_id, user_id, title, timestamp_str)
            )

            for msg in messages:
                cursor.execute(
                    "INSERT INTO chat_messages (conversation_id, role, content) VALUES (%s, %s, %s)",
                    (new_id, msg['role'], msg['content'])
                )
            count += 1

        conn.commit()
        return jsonify({
            'message': f'Berhasil memigrasi {count} percakapan.',
            'migrated_count': count
        }), 200

    except Exception as e:
        if conn: conn.rollback()
        current_app.logger.error(f"[AI] migrate_from_json error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor: cursor.close()
        if conn: close_db_connection(conn)
