from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.db import models
from run import APP

migrate = Migrate(APP, models.db)
manager = Manager(APP)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
