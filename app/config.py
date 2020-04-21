import os
import pathlib

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Config:
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_ENABLED = False if os.getenv('CSRF_ENABLED') == 'false' else True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY", SECRET_KEY)


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = rf"sqlite:///{parent_dir}/db/dev-db.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = "it is secret"
    WTF_CSRF_ENABLED = False


class NoLoginTestingConfig(TestingConfig):
    LOGIN_DISABLED = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = rf"sqlite:///{parent_dir}/db/prod-db.sqlite"


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'no_login_test': NoLoginTestingConfig,
    'production': ProductionConfig,
}
