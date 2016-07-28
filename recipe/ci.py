import logging
import os.path

from jenkins import Jenkins
from jinja2 import Environment
from jinja2 import FileSystemLoader

logger = logging.getLogger('recipe')


class Env(object):
    __env = None

    def __init__(self):
        if Env.__env is None:
            template_home = os.path.normpath(os.path.join(__file__, '..', 'templates'))
            Env.__env = Environment(loader=FileSystemLoader(template_home))

    @staticmethod
    def render(name, context):
        template = Env.__env.get_template(name)
        return template.render(**context)


def create_jenkins_jobs(project_slug, repo=None, jenkins_url=None):
    if repo is None:
        repo = ''
    if jenkins_url is None:
        jenkins_url = 'http://scdfis01:8080'

    project_slug = project_slug.capitalize()

    logger.info('Login in %s', jenkins_url)
    client = Jenkins(jenkins_url, 'recipe', 'recipe')

    env = Env()
    jobs = reversed(['Analysis', 'UT', 'Build', 'IT', 'AT', 'Deploy'])
    context = dict(project_slug=project_slug,
                   repo=repo,
                   credential='30ba71ab-eec8-4082-b171-8edecfe076de'
                   )
    for prefix in jobs:
        template_name = '{0}.xml'.format(prefix.lower())
        job_name = '{0}_{1}'.format(prefix, project_slug)
        config = env.render(template_name, context)
        logger.info('Creating jenkins job %s', job_name)
        client.create_job(job_name, config)

    logger.info('Create jenkins view %s', project_slug)
    config = env.render('view.xml', context)
    client.create_view(project_slug, config)


if __name__ == '__main__':
    create_jenkins_jobs('Sunny')
