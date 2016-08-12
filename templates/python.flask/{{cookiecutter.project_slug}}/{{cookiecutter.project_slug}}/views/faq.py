from {{cookiecutter.project_slug}} import app
from {{cookiecutter.project_slug}} import __version__


@app.route("/version", methods=['GET'])
def version():
    return __version__

@app.route("/faq.htm")
def faq():
    return "<!--Newegg-->"