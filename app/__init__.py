from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

app.config.from_object('config')

# Database Object
db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')	

@app.route('/admin')
def professors():
	return render_template('admin.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/createProject')
def createProject():
	return render_template('createProject.html')

@app.route('/view')
def view():
	return render_template('view.html')

@app.route('/createProposal')
def proposal():
	return render_template('createProposal.html')