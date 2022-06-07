from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def config(app):
    db.init_app(app)
