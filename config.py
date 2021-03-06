import os

basedir = os.path.abspath(os.path.dirname(__file__))
config_name = os.getenv('APP_ENVIRONMENT', 'development')


class Config:
    def __init__(self):
        pass

    FIREBASE_REALTIME_DB_URL = os.getenv('FR_REALTIME_DB', None)
    CREDENTIALS_PATH = 'credentials/serviceAccountKey.json'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig
}

current_config = config.get(config_name)
