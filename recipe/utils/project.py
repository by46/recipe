import os.path
import re
import sys

_RE_PROJECT_NAME = re.compile('^[A-Za-z0-9_\-]{1,50}$', re.MULTILINE)


def valid_project_slug(name):
    return _RE_PROJECT_NAME.match(name)


def get_templates_home():
    return [os.path.join(sys.prefix, 'recipe', 'templates'),
            os.path.join(os.path.expanduser('~/recipe/templates'))]
