import sys

from recipe.commands import Command
from recipe.utils import create_jenkins_jobs


class DeployCommand(Command):
    name = "deploy"

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('deploy', help='Create CI task on Jenkins.')
        parser.add_argument('-r', '--repo', dest='repo',
                            help='the git repo on trgit2, like: https://trgit2/dfis/recipe.git')
        parser.add_argument('name')

    def run(self):
        project_slug = self.options.name
        repo = self.options.repo
        try:
            jenkins = self.config.get_tuple('jenkins', 'url', 'user', 'password')
            create_jenkins_jobs(project_slug, repo, jenkins=jenkins)
        except Exception as e:
            self.logger.exception(e)
            sys.exit(1)
