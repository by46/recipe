from flask import render_template

from {{cookiecutter.project_slug}}.db import DataAccess
from {{cookiecutter.project_slug}} import bp


@bp.route("/version", methods=['GET'])
def version():
    return render_template('version.html', version=DataAccess.get_version())

@bp.route("/faq.htm")
def faq():
    return render_template('faq.html')