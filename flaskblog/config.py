import os
import configparser

config = configparser.RawConfigParser()
config.read(r'flaskblog/config.ini')


class Config:
    SECRET_KEY = config.get("configurations", 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get(
        "configurations", 'SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get("configurations", 'MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get("configurations", 'MAIL_USERNAME')
    MAIL_PASSWORD = config.get("configurations", 'MAIL_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
