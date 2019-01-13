import os

HOME = os.path.expanduser('~')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('FLASK_DEBUG') or False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or f'sqlite:///{HOME}/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
