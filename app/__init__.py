from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import select
from config import app_config, Config, DevelopmentConfig
import json
from datetime import datetime
db = SQLAlchemy()
from .projects.models import Project

def create_app(config_name):
	# WSGI application object
	app = Flask(__name__)
	app.config.from_object(DevelopmentConfig)
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
		project = []
		result = Project.query.all()
		for row in result:
			#If the date is today, it gives the time in AM/PM, otherwise gives the date in m/d/Y
			dateSwitcher = "on " + row.date.strftime('%m/%d/%Y')
			if datetime.today().strftime('%m/%d/%Y') == row.date.strftime('%m/%d/%Y'):
				dateSwitcher = "at " + row.date.strftime('%I:%M%p')
			project.append([row.id, row.title, row.desc, row.author, dateSwitcher, row.views, row.visibility, row.sponsors, row.locked])
		return render_template('projects.html', projects=project)

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

	return app
