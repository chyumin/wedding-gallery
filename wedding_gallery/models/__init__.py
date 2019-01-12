from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from wedding_gallery import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# Disable warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)
DBSession = db.session
