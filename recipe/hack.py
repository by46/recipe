import logging
import os

from cookiecutter.hooks import _HOOKS

_HOOKS_EXT = ['.py', '.sh']


def find_hooks():
    """
    Must be called with the project template as the current working directory.
    Returns a dict of all hook scripts provided.
    Dict's key will be the hook/script's name, without extension, while
    values will be the absolute path to the script.
    Missing scripts will not be included in the returned dict.
    """
    hooks_dir = 'hooks'
    r = {}
    logging.debug('hooks_dir is {0}'.format(hooks_dir))
    if not os.path.isdir(hooks_dir):
        logging.debug('No hooks/ dir in template_dir')
        return r
    for f in os.listdir(hooks_dir):
        basename, ext = os.path.splitext(os.path.basename(f))
        if basename in _HOOKS and ext in _HOOKS_EXT:
            r[basename] = os.path.abspath(os.path.join(hooks_dir, f))
    return r


def patch():
    from cookiecutter import hooks
    hooks.find_hooks = find_hooks
