from YAF import db
from YAF.models import User


from configparser import SafeConfigParser

config = SafeConfigParser()
config.read('control.cfg')
db.create_all()

if __name__ == '__main__':
    user = User(username=config.get('admin', 'username'), password=config.get('admin', 'password'))
    db.session.add(user)
    db.session.commit()
    print('[+] Done!')