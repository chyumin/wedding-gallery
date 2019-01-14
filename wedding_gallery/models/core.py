from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from wedding_gallery.models import db
from wedding_gallery import login_manager


class GalleryUser(UserMixin, db.Model):
    __tablename__ = 'gallery_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String(128), nullable=False)
    master = db.Column(db.Boolean, nullable=False, server_default='0')
    photos = db.relationship('Photo', backref='owner')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String, nullable=False)
    approved = db.Column(db.Boolean, nullable=False, server_default='0')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('gallery_user.id'))


class Like(db.Model):
    __tablename__ = 'like'
    user_id = db.Column(db.Integer, db.ForeignKey('gallery_user.id'))
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'))
    __table_args__ = (db.PrimaryKeyConstraint('user_id', 'photo_id'), )


@login_manager.user_loader
def load_user(id_):
    return GalleryUser.query.get(int(id_))
