from Flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from models import User, Progress
from database import db

pengaturan_bp = Blueprint('pengaturan', __name__)
@pengaturan_bp.route('/settings_user', methods=['GET', 'POST'])
@user_required
def pengaturan():
    user = User.query.get(current_user.id)
    if request.method == 'POST':
        new_email = request.form.get('email')
        new_password = request.form.get('password')
        if new_email:
            user.email = new_email
        if new_password:
            user.set_password(new_password)
        db.session.commit()
        flash('Pengaturan berhasil diperbarui!', 'success')
        return redirect(url_for('pengaturan.pengaturan'))
    return render_template('user/pengaturan.html', user=user)
