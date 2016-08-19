"""{{cookiecutter.project_slug}}

"""
import os

from flask import Flask
from flask_cors import CORS
from flask_log import Log
from flask_restful import Api

__version__ = '0.0.1'
__author__ = 'Recipe'

prefix = '/{0}'.format(__name__)
static_url_path = '/{0}/static'.format(__name__)

app = Flask(__name__, static_url_path=static_url_path)
bp = Blueprint(__name__, __name__, url_prefix=prefix)


app.config.from_object('config.default')
key = 'ENV'
if key not in os.environ:
    os.environ[key] = 'development'

env = os.environ.get(key)
app.config.from_object('config.{0}'.format(env.lower()))
app.config['VERSION'] = __version__

# Config restful
api = Api(app, prefix=prefix)

# Config CORS
CORS(app)

# Config Logger
Log(app)

from {{cookiecutter.project_slug}} import views

app.register_blueprint(bp)
