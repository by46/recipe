"""{{cookiecutter.project_slug}}

"""
import os

from flask import Flask
from flask_cors import CORS
from flask_log import Log

__version__ = '0.0.1'
__author__ = 'Recipe'

app = Flask(__name__)

from {{cookiecutter.project_slug}} import views

__all__ = ['views']

app.config.from_object('config.default')
key = 'ENV'
if key not in os.environ:
    os.environ[key] = 'development'

env = os.environ.get(key)
app.config.from_object('config.{0}'.format(env.lower()))
app.config['VERSION'] = __version__



# Config CORS
CORS(app, resources={'*': {"origins": "*", "methods": "*", "allow-headers": "Content-Type"}})

# Config Logger
Log(app)
