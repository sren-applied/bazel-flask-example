from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tempfile import mktemp


def create_app(config_filename="src.python.ws.conf.BaseConfig"):
    app = Flask(__name__)

    db = SQLAlchemy()
    db_name = 'users.db'

    app.config['TEMPDIR'] = mktemp()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
    app.config['APPLICATION_DB'] = db
    db.init_app(app)

    app.config.from_object(config_filename)
    from src.python.ws.home import home

    app.register_blueprint(home)

    return app


