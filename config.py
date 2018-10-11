class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    # Show Flask debug info
    DEBUG = True

    #Databse connector
    SQLALCHEMY_DATABASE_URI = 'mysql://marketplace:seniordesign@localhost/marketplace'

    # Show SQL Alchemy debug info
    SQLALCHEMY_ECHO = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application threads.
    # 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Secure key for signing data
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
