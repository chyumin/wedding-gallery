from flask import render_template

from wedding_gallery import app


@app.route('/')
def index():
    return render_template('index.html', foo=42)
