from flask import flash, redirect, render_template, url_for

from wedding_gallery import app
from wedding_gallery.forms import CreateUserForm
from wedding_gallery.models import core, DBSession


@app.route('/users')
def users():
    template_args = {
        'title': 'Users'
    }
    return render_template('users.html', **template_args)


@app.route('/users/create_user')
def create_user():
    form = CreateUserForm()
    template_args = {
        'form': form,
        'title': 'Create User'
    }
    return render_template('create_user.html', **template_args)


@app.route('/users/do_create_user', methods=['POST'])
def do_create_user():
    form = CreateUserForm()
    if not form.validate_on_submit():
        flash('Could not create user', 'error')
        return redirect(url_for('users'))
    username = form.username.data
    password = form.password.data
    new_user = core.GalleryUser(username=username, password=password)
    DBSession.add(new_user)
    DBSession.commit()
    flash(f'User {username} created')
    return redirect(url_for('users'))
