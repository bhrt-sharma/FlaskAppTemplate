import logging
from flask import Flask
from config import ServiceConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(ServiceConfig)

    FORMAT = '%(asctime)-15s [%(levelname)s] [%(filename)s:%(lineno)s]: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, filename="logs/save_logs.out")

    from routes import template_app

    app.register_blueprint(template_app)

    return app
