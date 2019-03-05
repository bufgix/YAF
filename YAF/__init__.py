from flask import Flask
from flask_ngrok import run_with_ngrok
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from YAF.config import Config as flask_conf

from configparser import SafeConfigParser
import os


app = Flask(__name__)
app.config.from_object(flask_conf)
app.url_map.strict_slashes = False


db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'main'

config = SafeConfigParser()
config.read(os.path.join(os.path.dirname(app.root_path), 'control.cfg'))
run_with_ngrok(app)


from YAF import views
