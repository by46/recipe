from flask_restful import Resource

from {{cookiecutter.project_slug}} import api
from {{cookiecutter.project_slug}}.db import DataAccess


@api.resource('/api/v1/version')
class Version(Resource):
    @staticmethod
    def get():
        return dict(version=DataAccess.get_version())
