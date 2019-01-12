from wedding_gallery.models import db


class GalleryUser(db.Model)
    __tablename__ = 'gallery_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    master = db.Column(db.Bool, nullable=False, server_default='0')


class Photos(db.Model)
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)


class Gallery(db.Model)
    __tablename__ = 'gallery'
    id = db.Column(db.Integer, primary_key=True)

