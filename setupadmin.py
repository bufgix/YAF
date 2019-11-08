from YAF import db
from YAF.models import User

from configparser import ConfigParser

config = ConfigParser()
config.read('control.cfg')
db.create_all()

if __name__ == '__main__':
    exists = User.query.first()
    if exists:
        print("Updating admin information...")
        exists.username = config.get('admin', 'username')
        exists.password = config.get('admin', 'password')
        db.session.commit()

    else:
        print("Create new admin user...")
        user = User(username=config.get('admin', 'username'),
                    password=config.get('admin', 'password'))
        db.session.add(user)
        db.session.commit()
    print('[+] Done!')
