from flask import render_template

from {{cookiecutter.project_slug}} import app


@app.route("/version", methods=['GET'])
def version():
    return render_template('version.html', version=app.config['VERSION'])

@app.route("/faq.htm")
def faq():
    return render_template('faq.html')