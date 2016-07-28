import os
import os.path
from json import dump
from json import load


def load_project_template(root):
    if not os.path.isdir(root):
        raise Exception('root exists')
    return {os.path.basename(tmp): os.path.join(root, tmp) for tmp in os.listdir(root) if
            os.path.isdir(os.path.join(root, tmp))}


def gen_cookie_cutter_meta_json(home, project_slug):
    json_path = os.path.join(home, 'cookiecutter.json')
    with open(json_path, 'rb') as f:
        obj = load(f)

    obj['project_slug'] = project_slug
    with open(json_path, 'wb') as f:
        dump(obj, f)
