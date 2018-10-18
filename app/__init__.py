from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import select
from config import app_config, Config, DevelopmentConfig
import json
from datetime import datetime
db = SQLAlchemy()

def create_app(config_name):
	# WSGI application object
	app = Flask(__name__)
	app.config.from_object(DevelopmentConfig)
	app.config.from_pyfile('../config.py')
	db.init_app(app)


	# FIXME: These should be moved to the modules
	@app.route('/')
	def index():
		return render_template('index.html')

	@app.route('/admin')
	def professors():
		return render_template('admin.html')

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

	from .projects import projects as projects_blueprint
	app.register_blueprint(projects_blueprint, url_prefix='/projects')

	return app
