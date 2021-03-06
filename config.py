import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    # e.g. export SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/book'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development':  DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestingConfig,
}
