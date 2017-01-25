import logging
import os
import os.path
import re
import sys
from json import dump
from json import load

import six

_RE_PROJECT_NAME = re.compile('^[A-Za-z0-9_\-]{1,50}$', re.MULTILINE)

logger = logging.getLogger('recipe')


def valid_project_slug(name):
    return _RE_PROJECT_NAME.match(name)


def get_templates_home():
    return ['templates', os.path.join(sys.prefix, 'recipe', 'templates'),
            os.path.join(os.path.expanduser('~/.recipe/templates'))]


def load_project_template(roots):
    templates = dict()
    if isinstance(roots, six.string_types):
        roots = [roots]
    for root in roots:
        if not os.path.isdir(root):
            continue
        try:
            for tmp in os.listdir(root):
                full_path = os.path.join(root, tmp)
                if os.path.isdir(full_path):
                    template_name = os.path.basename(full_path).lower()
                    if template_name in templates:
                        logger.warning('Project template %s in %s has already exists in %s, We will ignore it.',
                                       template_name, root,
                                       templates[template_name])
                        continue
                    templates[template_name] = full_path
        except Exception as e:
            logger.warning(u"Load templates in '%s' : %s", root, e)
    return templates


def gen_cookie_cutter_meta_json(home, project_slug, group_slug=None, author=None, env=None):
    json_path = os.path.join(home, 'cookiecutter.json')
    with open(json_path, 'rb') as f:
        obj = load(f)

    obj['project_name'] = project_slug
    if group_slug:
        obj['group_name'] = group_slug
    if author is not None:
        obj['author'] = author
    if env is  None:
        env = "gdev"
    obj['env'] = env
    with open(json_path, 'wb') as f:
        dump(obj, f)
