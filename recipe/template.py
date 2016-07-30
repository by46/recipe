import logging
import os
import os.path
from json import dump
from json import load

import six

logger = logging.getLogger('recipe')


def load_project_template(roots):
    templates = dict()
    if isinstance(roots, six.string_types):
        roots = [roots]
    for root in roots:
        if not os.path.isdir(root):
            continue
        for tmp in os.listdir(root):
            full_path = os.path.join(root, tmp)
            if os.path.isdir(full_path):
                template_name = os.path.basename(full_path).lower()
                if template_name in templates:
                    logger.warning('Project template %s in %s has already exists in %s, We will override it.',
                                   template_name, root,
                                   templates[template_name])
                templates[template_name] = full_path
    return templates


def gen_cookie_cutter_meta_json(home, project_slug):
    json_path = os.path.join(home, 'cookiecutter.json')
    with open(json_path, 'rb') as f:
        obj = load(f)

    obj['project_slug'] = project_slug
    with open(json_path, 'wb') as f:
        dump(obj, f)
