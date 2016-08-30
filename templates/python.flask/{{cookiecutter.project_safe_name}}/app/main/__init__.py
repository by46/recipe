from flask import Blueprint

url_prefix = '/{{cookiecutter.project_slug}}'
main = Blueprint('main', __name__, url_prefix=url_prefix)

from . import views
