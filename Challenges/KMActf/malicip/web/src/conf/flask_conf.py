
class Config(object):
    DB_SERVER = "db"
    DB_PORT = 3306
    DB_USER = "malicip"
    DB_PASSWORD = "malicip"
    DB_DBNAME = "malicip"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = "127.0.0.1"
    DB_PORT = 33306

class TestingConfig(Config):
    TESTING = True

