from app import db

class Project(db.Model):

	__tablename__ = 'projects'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60), index=True, unique=True)
	desc = db.Column(db.String(5000))
	author = db.Column(db.String(50), index=True)
	date = db.Column(db.DateTime, index=True)
	views = db.Column(db.Integer, index=True)
	visibility = db.Column(db.String(8), server_default="public")
	sponsors = db.Column(db.String(500))
	locked = db.Column(db.Boolean, server_default='0')
	

class Proposal(db.Model):
	__tablename__ = 'proposals'
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60), index=True, unique=True)
	desc = db.Column(db.String(5000))
	author = db.Column(db.String(50), index=True)
	date = db.Column(db.DateTime, index=True)
	views = db.Column(db.Integer, index=True)
	sponsors = db.Column(db.String(500))
	