# manage.py
from flask_migrate import MigrateCommand
from flask_script import Server, Shell, Manager

from app import app


manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
