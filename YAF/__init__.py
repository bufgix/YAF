from flask import Flask
from YAF.flask_ngrok import run_with_ngrok
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user

from YAF.config import Config as flask_conf

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

from YAF import views
from YAF.models import User

def start_server(args):
    db.create_all()
    exists = User.query.first()
    if args.username and args.password:
        if exists:
            print("Updating admin information...")
            exists.username = args.username
            exists.password = args.password
        else:
            print("Create admin profile...")
            admin = User(username=args.username, password=args.password)
            db.session.add(admin)
        db.session.commit()
    else:
        if not exists:
            print("No admin profile found. Set admin name and password !")
            return

    if not args.no_ngrok:
        run_with_ngrok(app)
    app.run()
