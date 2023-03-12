import os

from flask import Flask

from config import Config
from maintenance_accounting_app.extensions import db

def create_app(config_class=Config):
    """
    Application factory function
    """
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
