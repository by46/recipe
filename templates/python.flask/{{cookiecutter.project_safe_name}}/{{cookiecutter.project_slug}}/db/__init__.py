from {{cookiecutter.project_slug}} import app


class DataAccess(object):
    @staticmethod
    def get_version():
        return app.config['VERSION']
