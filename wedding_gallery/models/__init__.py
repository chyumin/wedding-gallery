from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from cerberus import app

db = SQLAlchemy(app, session_options={'autocommit': True})
migrate = Migrate(app, db)
DBSession = db.session
