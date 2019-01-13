from flask import render_template

from wedding_gallery import app


@app.route('/users')
def users():
    template_args = {
        'title': 'Users'
    }
    return render_template('users.html', **template_args)
