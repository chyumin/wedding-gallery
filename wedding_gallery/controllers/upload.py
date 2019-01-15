from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from wedding_gallery import app
from wedding_gallery.models import core, DBSession


@login_required
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif']


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = [f for f in request.files.getlist('file') if f and f.filename]
        if not files:
            flash('No selected file')
            return redirect(request.url)
        for file in files:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = url_for('static', filename=filename)
                file.save('wedding_gallery' + path)
                photo = core.Photo(link=path, user_id=current_user.id)
                DBSession.add(photo)
            DBSession.commit()
        flash(f'{len(files)} photos uploaded!')
        return redirect(url_for('upload'))

    template_args = {
        'title': 'Upload Photos'
    }
    return render_template('upload.html', **template_args)
