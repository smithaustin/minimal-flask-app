from flask import Flask, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from configparser import ConfigParser
from models import db

config = ConfigParser()
config.read('config.ini')
db_config = config["database"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_config["user"]}:{db_config["password"]}@localhost/{'
db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def dev():
    app.run(debug=True)


@app.route('/test')
def index():
    return "Config Success"

if __name__ == "__main__":
    manager.run()
