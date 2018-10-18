from flask import render_template, request, flash

from . import projects
from .models import Project
from .. import db

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

@projects.route('/createProject/add', methods=['GET', 'POST'])
def add_project():
    project = Project(title = request.form.get(title),
                        desc = request.form.get(description),
                        date = request.form.get(lockout_date),
                        visibility = request.form.get(visibility),
                        sponsors = request.form.get(sponsors),
                        locked = request.form.get(locked)
                        )

    try:
        db.session.add(project)
        db.session.commit()
        flash('Successfully added project')
    except:
        flash('An error occurred adding project to the database')
