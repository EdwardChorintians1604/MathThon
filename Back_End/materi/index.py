from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify, g, abort, current_app, Flask, send_from_directory, make_response
from .security_for_web import login_required, admin_required, user_required, generate_key
from .database import get_db_connection
from werkzeug.utils import secure_filename
import os

materi_matematika_bp = Blueprint('materi_matematika', __name__, template_folder='templates/materi_matematika', static_folder='static/materi_matematika')

@app.route('user/materi/')
@login_required
def index():
    conn = get_db_connection()
    materi_list = conn.execute('SELECT * FROM materi_matematika').fetchall()
    conn.close()
    return render_template('index.html', materi_list=materi_list)

# Endpoint API: Daftar materi (JSON)
@materi_matematika_bp.route('/api/materi', methods=['GET'])
@login_required
def api_materi_list():
    conn = get_db_connection()
    count = request.args.get('count', type=int)  # Parameter untuk jumlah materi yang ingin diambil
    materi_list = conn.execute('SELECT * FROM materi_matematika').fetchall()
    conn.close()
    # Jika count diberikan, batasi jumlah materi yang dikembalikan
    if count and count > 0:
        materi_list = materi_list[:count]
    materi_json = [dict(row) for row in materi_list]
    return jsonify(materi_json)

# Endpoint API: Detail materi (JSON)
@materi_matematika_bp.route('/api/materi/<int:materi_id>', methods=['GET'])
@login_required
def api_materi_detail(materi_id):
    conn = get_db_connection()
    materi = conn.execute('SELECT * FROM materi_matematika WHERE id = ?', (materi_id,)).fetchone()
    conn.close()
    if materi is None:
        return jsonify({'error': 'Materi tidak ditemukan'}), 404
    return jsonify(dict(materi))
