from logging.config import dictConfig

from flask import Flask
from flask_rebar import Rebar, SwaggerV3Generator

from app.logging.config import config

rebar = Rebar()
v1_registry = rebar.create_handler_registry(
    prefix='/v1',
    swagger_path='/apidocs',
    swagger_ui_path='/apidocs-ui',
    swagger_generator=SwaggerV3Generator(title="Face Recognition",
                                         description="Face Recognition REST Service using DLIB")
)


def create_app() -> Flask:
    dictConfig(config=config)
    app = Flask(__name__)
    app.config.from_envvar("APP_CONFIG")
    rebar.init_app(app)
    return app
