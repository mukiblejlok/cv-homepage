from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
# from flask_cors import CORS
from flask_moment import Moment

from .config import config, Config


db = SQLAlchemy()
sess = Session()
moment = Moment()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'please login'
login_manager.login_message_category = 'danger'


def create_app(config_name):
    from .models import User

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.app_context().push()
    sess.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    from .cv import cv as cv_blueprint
    app.register_blueprint(cv_blueprint, url_prefix='/cv')
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    return app


if __name__ == "__main__":
    app = create_app(config_name='development')
    app.run(host='0.0.0.0', debug=True)

