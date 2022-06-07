from os import getenv

from dotenv import load_dotenv


load_dotenv()


def config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['X_GLB_TOKEN'] = getenv('X_GLB_TOKEN')
