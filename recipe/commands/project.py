import os
import shutil
import sys
import tempfile

from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter

from recipe.ci import create_jenkins_jobs
from recipe.commands import Command
from recipe.template import gen_cookie_cutter_meta_json
from recipe.template import load_project_template
from recipe.utils import get_templates_home
from recipe.utils import valid_project_slug


class ProjectCommand(Command):
    name = 'startproject'

    def __init__(self, options):
        super(ProjectCommand, self).__init__(options)

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('startproject', help='startproject help')
        parser.add_argument('-t', '--template', dest='template', default='python.flask', help="project template name")
        parser.add_argument('-o', '--output-dir', dest='out', default='.',
                            help='Where to output the generated project dir into')
        parser.add_argument('-r', '--repo', dest='repo',
                            help='the git repo on trgit2, like: https://trgit2/dfis/recipe.git')
        parser.add_argument('name')

    def run(self):
        args = self.options
        project_slug = args.name

        # check project name
        if not valid_project_slug(project_slug):
            self.logger.critical(
                'Project name is invalid, just contain alpha, digit, underscore(_), and max length is 50.')

        templates_home = get_templates_home()
        if templates_home is None:
            self.logger.critical('Checking project templates does not exists')

        self.logger.info('Loading project templates from %s', templates_home)
        templates = load_project_template(templates_home)

        if args.template not in templates:
            self.logger.error('%s does not exists', args.template)
            sys.exit(1)

        temp_work_dir = tempfile.mkdtemp(prefix='recipe-{0}-'.format(project_slug))
        os.rmdir(temp_work_dir)
        shutil.copytree(templates[args.template], temp_work_dir)
        self.logger.info('Copying project templates into %s', temp_work_dir)

        if not os.path.isdir(args.out):
            self.logger.info('Creating output dir %s', args.out)
            os.makedirs(args.out)

        try:
            gen_cookie_cutter_meta_json(temp_work_dir, project_slug)
            cookiecutter(temp_work_dir, no_input=True, output_dir=args.out)

            create_jenkins_jobs(project_slug, args.repo)

        except OutputDirExistsException:
            self.logger.warning("%s directory already exists, please ensure it does not exists. ",
                                os.path.join(args.out, project_slug))
            sys.exit(2)
        except Exception as e:
            self.logger.exception(e)
            sys.exit(3)
