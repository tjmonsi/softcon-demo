# Import flask and template operators
from flask import Flask
from config import Config

def create_app(config_class=Config):
    # Define the WSGI application object
    app = Flask(__name__)

    # Configurations
    app.config.from_object(config_class)

    # register errors
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.api.base import bp as base_bp
    app.register_blueprint(base_bp)

    from app.api.v0 import bp as v0_bp
    app.register_blueprint(v0_bp)

    return app
