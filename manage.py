from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from cmdb import app
from exts import db
from apps.cmdb import models as cmdb_models

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)

CMDBUser = cmdb_models.CMDBUser

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cmdb_user(username, password, email):
    user = CMDBUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('用户创建成功')

if __name__ == '__main__':
    manager.run()