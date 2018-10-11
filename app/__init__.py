from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import app_config

# Database Object
db = SQLAlchemy()

def create_app(config_name):
	# WSGI application object
	app = Flask(__name__)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('../config.py')
	db.init_app(app)


	# FIXME: These should be moved to the module __init__.py files
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

	migrate = Migrate(app, db)

	from app.projects import models

	return app
