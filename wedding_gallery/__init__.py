from flask import Flask
from wedding_gallery.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from wedding_gallery.controllers import gallery, users
