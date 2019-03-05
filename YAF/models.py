from flask_login import UserMixin

from YAF import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))
    current_page = db.Column(db.String)
    _records = db.Column(db.String, default='')

    @property
    def records(self):
        return [record for record in self._records.split(';')]

    @records.setter
    def records(self, val):
        self._records += f";{val}"
    