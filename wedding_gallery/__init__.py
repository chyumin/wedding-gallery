from flask import Flask
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from wedding_gallery.controllers import auth, gallery, users
