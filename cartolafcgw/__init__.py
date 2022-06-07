from flask import Flask

from cartolafcgw import settings, database, migrate, cli, routes


def create_app():
    app = Flask(__name__)
    settings.config(app)
    database.config(app)
    migrate.config(app)
    cli.config(app)
    routes.config(app)
    return app
