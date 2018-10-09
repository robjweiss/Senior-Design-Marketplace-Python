#For development configuration
# The Keys and DB URL will be changed before deployment to server

DEBUG = True

# Application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# DB
SQLALCHEMY_DATABASE_URI = 'mysql://marketplace:seniordesign@localhost/marketplace'
#DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_ECHO = True

# Application threads.
# 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Secure key for signing data
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
