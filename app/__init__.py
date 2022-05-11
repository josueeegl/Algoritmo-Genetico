from flask import Flask
from config import Config

from .routes import ini

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

app.register_blueprint(ini, url_prefix="/")