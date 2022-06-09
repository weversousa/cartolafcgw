from os import getenv

from dotenv import load_dotenv


load_dotenv()


def config(app):
    DATABASE_URL = getenv('DATABASE_URL').replace('s:', 'sql:')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['X_GLB_TOKEN'] = getenv('X_GLB_TOKEN')
