from flask import render_template
from datetime import datetime
from . import projects
from . import view
from .models import Project

@projects.route('/', methods=['GET', 'POST'])
def get_projects():
	project_list = []
	result = Project.query.all()
	for row in result:
		#If the date is today, it gives the time in AM/PM, otherwise gives the date in m/d/Y
		dateSwitcher = "on " + row.date.strftime('%m/%d/%Y')
		if datetime.today().strftime('%m/%d/%Y') == row.date.strftime('%m/%d/%Y'):
			dateSwitcher = "at " + row.date.strftime('%I:%M%p')
		project_list.append([row.id, row.title, row.desc, row.author, dateSwitcher, row.views, row.visibility, row.sponsors, row.locked])
	return render_template('projects.html', projects=project_list)

@view.route('/<int:id>', methods=['GET', 'POST'])
def get_single_project(id):
	proj = Project.query.filter_by(id=id).first()
	dateSwitcher = "on " + proj.date.strftime('%m/%d/%Y')
	if datetime.today().strftime('%m/%d/%Y') == proj.date.strftime('%m/%d/%Y'):
		dateSwitcher = "at " + proj.date.strftime('%I:%M%p')
	return render_template('view.html', info=[proj.id, proj.title, proj.desc, proj.author, dateSwitcher, proj.views, proj.visibility, proj.sponsors, proj.locked])