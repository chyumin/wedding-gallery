from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

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
    photos = core.Photo.query.filter_by(approved=False).all()
    template_args = {
        'photos': photos,
        'title': 'Approve Photos'
    }
    return render_template('approve_photos.html', **template_args)


@app.route('/do_approve', methods=['POST'])
@util.require_master
def do_approve():
    photos_ids_list = request.form.getlist('checkbox-list')
    if not photos_ids_list:
        flash('No photos approved')
        return redirect(url_for('approve_photos'))
    query = DBSession.query(core.Photo).filter(
        core.Photo.id.in_(photos_ids_list)
    )
    query.update({
        core.Photo.approved: True
    }, synchronize_session=False)
    DBSession.commit()
    flash('Photos Approved!')
    return redirect(url_for('approve_photos'))


@app.route('/do_like')
def do_like():
    if current_user.is_anonymous:
        flash('Must be logged in to Like Photos')
        return jsonify({'not_logged': True})

    photo_id = request.args.get("photo_id")
    user_id = current_user.id
    if not photo_id or not user_id:
        flash('Failed to like')
        redirect(url_for('index'))
    like = DBSession.query(core.Like).\
        filter_by(user_id=user_id, photo_id=photo_id).first()
    if not like:
        like = core.Like(user_id=user_id, photo_id=photo_id)
        DBSession.add(like)
    else:
        DBSession.delete(like)
    DBSession.commit()
    photo = core.Photo.query.get(photo_id)
    return jsonify({'number_of_likes': photo.number_of_likes})
