from datetime import datetime

from wedding_gallery.models import db


class GalleryUser(db.Model):
    __tablename__ = 'gallery_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    master = db.Column(db.Boolean, nullable=False, server_default='0')


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, primary_key=True)
    approved = db.Column(db.Boolean, nullable=False, server_default='0')
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now)


class Likes(db.Model):
    __tablename__ = 'likes'

    gallery_user_id = db.Column(db.Integer, db.ForeignKey('gallery_user.id'), primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'), primary_key=True)
