class BaseConfig():
    DEBUG = True
    ENV = "development"

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 1800, "pool_pre_ping": True}
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/database.db"

    TEMPLATES_AUTO_RELOAD = True
