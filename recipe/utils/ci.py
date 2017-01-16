import json
import logging
import os.path
import webbrowser
import requests
import base64

from jenkins import Jenkins
from jinja2 import Environment
from jinja2 import FileSystemLoader

from .exception import CloudDataException
from .exception import JenkinsJobForbiddenException
from .exception import JenkinsViewForbiddenExceptioin
from .project import get_templates_home
from .project import load_project_template


logger = logging.getLogger('recipe')

NEXT_JOB_TEMPLATE = "<hudson.tasks.BuildTrigger>" \
                    "<childProjects>{0}</childProjects>" \
                    "<threshold>" \
                    "<name>SUCCESS</name>" \
                    "<ordinal>0</ordinal>" \
                    "<color>BLUE</color>" \
                    "<completeBuild>true</completeBuild>" \
                    "</threshold>" \
                    "</hudson.tasks.BuildTrigger>"


class JenkinsCI(object):
    def __init__(self, context_path=None):
        if not (context_path and os.path.exists(context_path)):
            context_path = os.path.normpath(os.path.join(__file__, '..', '..', 'ci'))
        self.__env = Environment(loader=FileSystemLoader(context_path))

    def render(self, name, context):
        template = self.__env.get_template(name)
        return template.render(**context)


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


def create_jenkins_jobs(project_name, repo=None, jenkins=None, template=None, browse=False, jobs=None,
                        cloud_data_url=None,
                        mail_list=None,
                        gdev=None,
                        gqc=None,
                        group=None,
                        gqc_replicas=1,
                        gdev_replicas=1):
    """

    :param project_name:
    :param repo:
    :param jenkins:
    :param template:
    :param browse:
    :param jobs:
    :param gqc:
    :param group:
    :param gdev:
    :param gdev_replicas:
    :param gqc_replicas:
    :param cloud_data_url:
    :param mail_list:
    :return ci jobs config:
    """
    if repo is None:
        repo = ''
    if jenkins is None:
        jenkins = 'http://10.16.76.197:8080', 'recipe', 'recipe'
    if cloud_data_url is None:
        cloud_data_url = 'http://10.16.75.24:3000/datastore/v1/dfis/dae/project:{0}'.format(project_name)
    if mail_list is None:
        mail_list = "$DEFAULT_RECIPIENTS"
    if gdev is None:
        gdev = 'http://scmesos02/{0}/version'.format(project_name)
    if gqc is None:
        gqc = 'http://s1qdfis02/{0}/version'.format(project_name)
    if group is None:
        group = 'recipe'

    jenkins_context_path = None
    jenkins_ci_path = None
    if template is not None:
        templates_home = get_templates_home()
        templates = load_project_template(templates_home)
        if template in templates:
            jenkins_context_path = os.path.join(templates[template], 'context')
            jenkins_ci_path = os.path.join(templates[template], 'ci')

    url, user, password = jenkins

    project_slug = project_name.capitalize()

    logger.info('Login in %s', url)
    client = Jenkins(url, user, password)

    logger.debug("Loading jenkins from %s", jenkins_context_path)
    logger.debug("Loading ci form %s", jenkins_ci_path)

    env = JenkinsContext(jenkins_context_path)
    ci_env = JenkinsCI(jenkins_ci_path)

    context = dict(
                   project_name=project_name,
                   project_slug=project_slug,
                   gdev_replicas=gdev_replicas,
                   gqc_replicas=gqc_replicas,
                   mail_list=mail_list,
                   gqc=gqc,
                   gdev=gdev,
                   group=group,
                   mail_trigger="FailureTrigger",
                   cloud_data=base64.b64encode(cloud_data_url).replace("=", "\="),
                   repo=repo)

    jenkins_jobs = reversed(env.jenkins_jobs())

    if not jobs:
        jobs = jenkins_jobs

    for job in jenkins_jobs:
        job_name = '{0}_{1}'.format(job, project_slug)
        if client.job_exists(job_name):
            client.delete_job(job_name)

    if client.view_exists(project_slug):
        client.delete_view(project_slug)

    job_count = len(jobs)
    job_max_index = job_count - 1

    job_conifg = []

    for i in xrange(job_count):
        prefix = jobs[i]
        job_name = '{0}_{1}'.format(prefix, project_slug)
        logger.info("Create Jenkins Job %s", job_name)
        template_name = '{0}.xml'.format(prefix.lower())
        context['job'] = prefix
        next_job_name = next_job(i, job_max_index, jobs)

        if next_job_name:
            context['build_trigger'] = NEXT_JOB_TEMPLATE.format(next_job_name + "_" + project_slug)
        else:
            context['build_trigger'] = ""
            context['mail_trigger'] = "AlwaysTrigger"

        config = env.render(template_name, context)
        client.create_job(job_name, config)
        logger.info("Create CI %s", job_name)
        template_name = "{0}.sh".format(prefix.lower())
        ci_config = ci_env.render(template_name, context)
        job_conifg.append({prefix: ci_config})

    logger.info('Create jenkins view %s', project_slug)
    config = env.render('view.xml', context)
    client.create_view(project_slug, config)

    if browse:
        view_url = '{0}/view/{1}'.format(url, project_slug)
        webbrowser.open(view_url)

    return job_conifg


def delete_jenkins_jobs(project_name, jenkins=None, template=None, jobs=None):
    """

    :param project_name:
    :param jenkins:
    :param template:
    :param jobs:

    :return:
    """

    if template is not None:
        templates_home = get_templates_home()
        templates = load_project_template(templates_home)
        if template in templates:
            jenkins_context_path = os.path.join(templates[template], 'context')
            env = JenkinsContext(jenkins_context_path)
            logger.debug("Loading jenkins from %s", jenkins_context_path)
            jobs = reversed(env.jenkins_jobs())

    if jenkins is None:
        jenkins = 'http://10.16.76.197:8080', 'recipe', 'recipe'

    url, user, password = jenkins

    project_slug = project_name.capitalize()

    logger.info('Login in %s', url)
    client = Jenkins(url, user, password)

    for job in jobs:
        job_name = '{0}_{1}'.format(job, project_slug)
        if client.job_exists(job_name):
            client.delete_job(job_name)

    if client.view_exists(project_slug):
        client.delete_view(project_slug)


def run_jenkins_job(project_name, job, jenkins=None):
    """

    :param project_name:
    :param job:
    :param jenkins:

    :return:
    """
    if project_name is None or job is None:
        return

    if jenkins is None:
        jenkins = 'http://10.16.76.197:8080', 'recipe', 'recipe'

    url, user, password = jenkins

    project_slug = project_name.capitalize()

    logger.info('Login in %s', url)
    client = Jenkins(url, user, password)

    job_name = "{0}_{1}".format(job, project_slug)
    client.build_job(job_name)


def next_job(index, max_index, jobs):
    next_index = index + 1
    if next_index <= max_index:
        return jobs[next_index]
    return ""

