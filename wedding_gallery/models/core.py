from datetime import datetime

from wedding_gallery.models import db


class GalleryUser(db.Model):
    __tablename__ = 'gallery_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String(128), nullable=False)
    master = db.Column(db.Boolean, nullable=False, server_default='0')


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, nullable=False)
    approved = db.Column(db.Boolean, nullable=False, server_default='0')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('gallery_user.id'))
