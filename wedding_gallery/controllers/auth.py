from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from wedding_gallery import app, forms
from wedding_gallery.models import core


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = core.GalleryUser.query.filter_by(
            username=form.username.data
        ).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Successfully Logged In!')
        return redirect(url_for('index'))
    template_args = {
        'form': form,
        'title': 'Sign In'
    }
    return render_template('login.html', **template_args)


@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully Logged Out')
    return redirect(url_for('index'))
