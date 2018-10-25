from flask import Blueprint

projects = Blueprint('projects', __name__)
view = Blueprint('view', __name__)

from . import views
