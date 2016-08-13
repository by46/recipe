from {{cookiecutter.project_slug}} import app


@app.route("/", methods=['GET'])
def index():
    return "hello, world"