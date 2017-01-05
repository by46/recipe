from recipe.commands import Command
from recipe.utils import create_jenkins_jobs


class DeployCommand(Command):
    name = "deploy"

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('deploy', help='Create CI task on Jenkins.')
        parser.add_argument('-t', '--template', dest='template', default='python.flask',
                            help="project template name")
        parser.add_argument('-r', '--repo', dest='repo',
                            help='the git repo on trgit2, like: http://trgit2/dfis/recipe.git')
        parser.add_argument('-b', '--browse', dest='browse', action='store_true', default=False,
                            help='Open jenkins views in default browser')
        parser.add_argument('-j', '--jobs', dest='jobs', default=None,
                            help='Jenkins jobs, like:["Analysis", "UT", "Build", "AT", "IT", "Deploy"]')
        parser.add_argument('-gr', '--gdev_replicas', dest='gdev_replicas', default=1,
                            help='gdev replicas')
        parser.add_argument('-qr', '--gqc_replicas', dest='gqc_replicas', default=1,
                            help='gqc replicas')
        parser.add_argument('-d', '--cloud_data', dest='cloud_data', default=None,
                            help='cloud data server')

        parser.add_argument('name')

    def run(self):
        self.logger.info("Create Jenkins CI Jobs starting.")
        project_slug = self.options.name
        repo = self.options.repo
        try:
            jenkins = self.config.get_tuple('jenkins', 'url', 'user', 'password')
            create_jenkins_jobs(project_slug, repo, jenkins=jenkins, template=self.options.template,
                                jobs=self.options.jobs,
                                gdev_replicas=self.options.gdev_replicas,
                                gqc_replicas=self.options.gqc_replicas,
                                cloud_data=self.options.cloud_data,
                                browse=self.options.browse)
            self.logger.info("Create Jenkins CI job success.")
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("Create Jenkins CI job failure.")
            raise e
