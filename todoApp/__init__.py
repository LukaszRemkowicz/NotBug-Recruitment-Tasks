from flask_migrate import Migrate

from models import db, app

migrate = Migrate(app, db)
