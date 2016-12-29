import json
import logging
import os.path
import webbrowser

from jenkins import Jenkins
from jinja2 import Environment
from jinja2 import FileSystemLoader

from .exception import JenkinsJobForbiddenException
from .exception import JenkinsViewForbiddenExceptioin
from .project import get_templates_home
from .project import load_project_template

logger = logging.getLogger('recipe')


class JenkinsContext(object):
    def __init__(self, context_path=None):
        if not (context_path and os.path.exists(context_path)):
            context_path = os.path.normpath(os.path.join(__file__, '..', '..', 'context'))
        self.__env = Environment(loader=FileSystemLoader(context_path))
        context_meta_path = os.path.join(context_path, 'context.json')
        with open(context_meta_path, 'rb') as f:
            self.__context_meta = json.load(f)

    def render(self, name, context):
        template = self.__env.get_template(name)
        return template.render(**context)

    @property
    def context(self):
        return self.__context_meta

    def jenkins_jobs(self):
        """create jenkins by this

        :return:
        """
        return self.context.get('jobs')


def create_jenkins_jobs(project_slug, repo=None, jenkins=None, template=None, browse=False):
    """

    :param project_slug:
    :param repo:
    :param jenkins:
    :param template:
    :param browse:
    :return:
    """
    if repo is None:
        repo = ''
    if jenkins is None:
        jenkins = 'http://scdfis01:8080', 'recipe', 'recipe'

    jenkins_context_path = None
    if template is not None:
        templates_home = get_templates_home()
        templates = load_project_template(templates_home)
        if template in templates:
            jenkins_context_path = os.path.join(templates[template], 'context')

    url, user, password = jenkins

    project_slug = project_slug.capitalize()

    logger.info('Login in %s', url)
    client = Jenkins(url, user, password)

    logger.debug("Loading jenkins from %s", jenkins_context_path)
    env = JenkinsContext(jenkins_context_path)
    context = dict(project_slug=project_slug,
                   repo=repo)

    for job in reversed(env.jenkins_jobs()):
        job_name = '{0}_{1}'.format(job, project_slug)
        if client.job_exists(job_name):
            raise JenkinsJobForbiddenException(job)
        logger.info('Is Jenkins Job %s exists?False', job_name)

    if client.view_exists(project_slug):
        raise JenkinsViewForbiddenExceptioin(project_slug)
    logger.info('Is Jenkins View %s exists?False', project_slug)

    for prefix in reversed(env.jenkins_jobs()):
        job_name = '{0}_{1}'.format(prefix, project_slug)
        logger.info("Create Jenkins Job %s", job_name)
        template_name = '{0}.xml'.format(prefix.lower())
        config = env.render(template_name, context)
        client.create_job(job_name, config)

    logger.info('Create jenkins view %s', project_slug)
    config = env.render('view.xml', context)
    client.create_view(project_slug, config)

    if browse:
        view_url = '{0}/view/{1}'.format(url, project_slug)
        webbrowser.open(view_url)
