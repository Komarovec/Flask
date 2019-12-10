from flask import Flask
from api.config import BaseConfig
from api.models.base import db
from .resources.urls import URLS
from flask_restful import Resource, Api
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    api = Api(app)
    Migrate(app, db)

    app.config.from_object(BaseConfig)
    db.init_app(app)

    for url in URLS:
        api.add_resource(*url[0], endpoint=url[1])

    return app
