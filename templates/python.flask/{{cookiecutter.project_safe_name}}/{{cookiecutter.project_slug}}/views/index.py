from flask import render_template

from {{cookiecutter.project_slug}} import bp


@bp.route("/", methods=['GET'])
def index():
    return render_template('index.html')