from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from wedding_gallery import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)
DBSession = db.session
