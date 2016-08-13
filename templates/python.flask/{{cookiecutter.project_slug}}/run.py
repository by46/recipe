"""deimos entry point

"""
import gevent.monkey
gevent.monkey.patch_all()

import logging
import os.path
from logging.handlers import RotatingFileHandler

from gevent.wsgi import WSGIServer

from {{cookiecutter.project_slug}} import app

if __name__ == '__main__':
    logs = app.config['LOG']
    if not os.path.exists(logs):
        os.makedirs(logs)

    handler = RotatingFileHandler(os.path.join(logs, 'error.log'), maxBytes=1024 * 1024 * 10, backupCount=10)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.logger.setLevel(logging.DEBUG)
    app.logger.info('{{cookiecutter.project_slug}} listening %s:%s', app.config['HTTP_HOST'], app.config['HTTP_PORT'])
    WSGIServer((app.config['HTTP_HOST'], app.config['HTTP_PORT']), application=app,
               log=app.config['WSGI_LOG']).serve_forever()
