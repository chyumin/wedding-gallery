from flask import render_template

from wedding_gallery import app
from wedding_gallery.models import core


@app.route('/')
def index():
    photos = core.Photo.query.filter_by(approved=True)
    template_args = {
        'photos': photos,
        'title': 'Wedding Gallery'
    }
    return render_template('index.html', **template_args)
