"""{{cookiecutter.project_slug}}

"""
from flask import Flask
from flask_restful import Api

__version__ = '0.0.1'
__author__ = 'benjamin.c.yan'

app = Flask(__name__)
app.config.from_object('config.default')
from deimos.views import Build
from deimos.views import Projects
from deimos.views import Project

api = Api(app)
api.add_resource(Build, '/build/<string:project_slug>')
api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<string:project_slug>')
