from flask import flash, redirect, render_template, request, url_for

from wedding_gallery import app, util
from wedding_gallery.models import core, DBSession


@app.route('/')
def index():
    photos = core.Photo.query.filter_by(approved=True)
    template_args = {
        'photos': photos,
        'title': 'Wedding Gallery'
    }
    return render_template('index.html', **template_args)


@app.route('/approve_photos')
@util.require_master
def approve_photos():
    photos = core.Photo.query.filter_by(approved=False)
    template_args = {
        'photos': photos,
        'title': 'Approve Photos'
    }
    return render_template('approve_photos.html', **template_args)


@app.route('/do_approve', methods=['POST'])
@util.require_master
def do_approve():
    photos_ids_list = request.form.getlist('checkbox-list')
    query = DBSession.query(core.Photo).filter(
        core.Photo.id.in_(photos_ids_list)
    )
    query.update({
        core.Photo.approved: True
    }, synchronize_session=False)
    DBSession.commit()
    flash('Photos Approved!')
    return redirect(url_for('approve_photos'))
