"""{{cookiecutter.project_slug}}

"""
import os

from flask import Flask
from flask_log import Log

__version__ = '0.0.1'
__author__ = 'Recipe'

app = Flask(__name__)

app.config.from_object('config.default')

key = 'ENV'
if key not in os.environ:
    os.environ[key] = 'development'

env = os.environ.get(key)
app.config.from_object('config.{0}'.format(env.lower()))
app.config['VERSION'] = __version__

# Config Logger
Log(app)

from {{cookiecutter.project_slug}} import views