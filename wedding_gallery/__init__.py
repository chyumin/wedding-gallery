from flask import Flask

app = Flask(__name__)

from wedding_gallery.controller import gallery
