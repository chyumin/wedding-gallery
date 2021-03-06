from flask import flash, redirect, render_template, request, url_for

from wedding_gallery import app, forms, util
from wedding_gallery.models import core, DBSession


@app.route('/users')
@util.require_master
def users():
    all_users = DBSession.query(core.GalleryUser).all()
    template_args = {
        'users': all_users,
        'title': 'Users'
    }
    return render_template('users.html', **template_args)


@app.route('/users/create_user')
@util.require_master
def create_user():
    form = forms.CreateUserForm()
    template_args = {
        'form': form,
        'title': 'Create User'
    }
    return render_template('create_user.html', **template_args)


@app.route('/users/do_create_user', methods=['POST'])
@util.require_master
def do_create_user():
    form = forms.CreateUserForm()
    if not form.validate_on_submit():
        flash('Could not create user', 'error')
        return redirect(url_for('users'))

    db_args = dict(username=form.username.data,
                   name=form.name.data,
                   master=form.master.data)
    new_user = core.GalleryUser(**db_args)
    new_user.set_password(form.password.data)

    DBSession.add(new_user)
    DBSession.commit()

    flash(f'User {form.name.data or form.username.data} created')
    return redirect(url_for('users'))


@app.route('/users/delete_users', methods=['POST'])
@util.require_master
def delete_users():
    users_ids_list = request.form.getlist('checkbox-list')
    query = DBSession.query(core.GalleryUser).\
        filter(core.GalleryUser.id.in_(users_ids_list))
    query.delete(synchronize_session=False)
    DBSession.commit()
    flash('Users deleted')
    return redirect(url_for('users'))
