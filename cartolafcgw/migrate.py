from flask_migrate import Migrate

from cartolafcgw.database import db
from cartolafcgw.models import *  # noqa


migrate = Migrate()


def config(app):
    migrate.init_app(app, db)
