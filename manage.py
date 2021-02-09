import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:puru2000@localhost:5432/northwind'

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
