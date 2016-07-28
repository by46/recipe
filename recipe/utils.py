import logging.config
import os.path
import re
import sys

_RE_PROJECT_NAME = re.compile('^[A-Za-z0-9_\-]{1,50}$', re.MULTILINE)


def get_package_name():
    return os.path.basename(os.path.dirname(__file__))


def config_logging(options):
    if options.verbose == 2:
        level = 'INFO'
    elif options.verbose >= 3:
        level = 'DEBUG'
    else:
        level = 'WARNING'

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'line': {
                'format': '%(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': level,
                'class': 'logging.StreamHandler',
                'formatter': 'line'
            }
        },
        'loggers': {
            'recipe': {
                'level': level,
                'handlers': ['console'],
                'propagate': False
            }
        }
    })


def get_templates_home():
    home = os.path.join(__file__, '..', '..', 'templates')
    if os.path.isdir(home):
        return os.path.normpath(home)

    home = os.path.join(sys.prefix, 'recipe', 'templates')
    if os.path.isdir(home):
        return home
    return None


def valid_project_slug(name):
    return _RE_PROJECT_NAME.match(name)
