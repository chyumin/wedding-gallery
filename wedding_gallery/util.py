from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user

from wedding_gallery import login_manager


def require_master(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            return login_manager.unauthorized()
        if not current_user.master:
            flash('Need to be logged in as Master')
            return redirect(url_for('index'))
        return fn(*args, **kwargs)
    return decorated_view
