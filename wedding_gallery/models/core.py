from wedding_gallery.models import db


class GalleryUser(db.Model):
    __tablename__ = 'gallery_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(64), nullable=False, unique=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text(128), nullable=False)
    master = db.Column(db.Boolean, nullable=False, server_default='0')

