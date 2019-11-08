from flask import Flask
from YAF.flask_ngrok import run_with_ngrok
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user

from YAF.config import Config as flask_conf

from configparser import SafeConfigParser
import os


def _cleanup():
    print("Stopping server...")
    logout_user()
    exit(0)


def cleanup(recv, frame):
    _cleanup()


app = Flask(__name__)
app.config.from_object(flask_conf)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'main'

config = SafeConfigParser()
config.read(os.path.join(os.path.dirname(app.root_path), 'control.cfg'))

from YAF import views


def start_server(args):
    if not args.no_ngrok:
        run_with_ngrok(app)
    app.run()
