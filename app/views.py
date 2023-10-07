from flask import Blueprint, render_template

views = Blueprint('flask_app', __name__)

@views.route("/")
def hello():
    return render_template("index.html")

@views.route("/people")
def people():
    return 'people'

@views.route("/projects")
def projects():
    return 'projects'

@views.route("/topics")
def topics():
    return 'topics'