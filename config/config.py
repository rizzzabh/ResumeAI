import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "kyahisecrethai"
    DEBUG = False
    TESTING = False
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
