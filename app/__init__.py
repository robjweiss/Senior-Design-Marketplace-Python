from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

app.config.from_object('config')

# Database Object
db = SQLAlchemy(app)

# temporary route
@app.route('/')
def hello_world():
    return 'Hello, World!'
