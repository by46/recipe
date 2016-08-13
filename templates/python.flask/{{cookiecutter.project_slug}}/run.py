"""deimos entry point

"""
import gevent.monkey
gevent.monkey.patch_all()



from gevent.wsgi import WSGIServer

from {{cookiecutter.project_slug}} import app

if __name__ == '__main__':
    app.logger.info('{{cookiecutter.project_slug}} listening %s:%s', app.config['HTTP_HOST'], app.config['HTTP_PORT'])
    
    WSGIServer((app.config['HTTP_HOST'], app.config['HTTP_PORT']), application=app,
               log=app.config['WSGI_LOG']).serve_forever()
