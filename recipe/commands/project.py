import os
import shutil
import sys
import tempfile

from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter

from recipe.commands import Command
from recipe.utils import create_jenkins_jobs
from recipe.utils import gen_cookie_cutter_meta_json
from recipe.utils import get_templates_home
from recipe.utils import load_project_template
from recipe.utils import valid_project_slug


class ProjectCommand(Command):
    """create a new template project

    """
    name = 'create'

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('create', help='Create project')
        parser.add_argument('-t', '--template', dest='template', default='python.flask', help="project template name")
        parser.add_argument('-o', '--output-dir', dest='out', default='.',
                            help='Where to output the generated project dir into')
        parser.add_argument('-d', '--deploy', dest='deploy', action='store_true',
                            help='Create CI task on Jenkins after create project successfully.')
        parser.add_argument('-r', '--repo', dest='repo',
                            help='the git repo on trgit2, like: http://trgit2/dfis/recipe.git')
        parser.add_argument('name')

    def run(self):
        try:
            self.logger.info("Create project starting...")
            args = self.options
            project_slug = args.name

            # check project name
            if not valid_project_slug(project_slug):
                self.logger.critical(
                    'Project name is invalid, just contain alpha, digit, underscore(_), and max length is 50.')

            templates_home = get_templates_home()

            self.logger.info('Loading project templates from %s', templates_home)
            templates = load_project_template(templates_home)

            if args.template not in templates:
                self.logger.error('Project template %s does not exists', args.template)
                sys.exit(1)

            temp_work_dir = tempfile.mkdtemp(prefix='recipe-{0}-'.format(project_slug))
            os.rmdir(temp_work_dir)
            shutil.copytree(templates[args.template], temp_work_dir)
            self.logger.info('Copying project templates into %s', temp_work_dir)

            if not os.path.isdir(args.out):
                self.logger.info('Creating output dir %s', args.out)
                os.makedirs(args.out)
            gen_cookie_cutter_meta_json(temp_work_dir, project_slug)

            cookiecutter(temp_work_dir, no_input=True, output_dir=args.out)

            if self.options.deploy:
                self.logger.info('Create jenkins CI jobs.')
                jenkins = self.config.get_tuple('jenkins', 'url', 'user', 'password')
                create_jenkins_jobs(project_slug, self.options.repo, jenkins=jenkins, template=self.options.template)

            self.logger.info('Create project %s success.', project_slug)
        except OutputDirExistsException:
            self.logger.error(
                u"Create Project failure : %s directory already exists, please ensure it does not exists. ",
                os.path.join(args.out, project_slug))
            self.logger.error("Create project %s failure.", project_slug)
            sys.exit(2)
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("Create project %s failure.", project_slug)
            raise e

    def _post_generate(self, temp_work_dir, output_project=None):
        """ convert CRLF to LF line separator

        Because cookcutter #405 bug

        :param temp_work_dir:
        :param output_project:
        :return:
        """
        post_path = os.path.join(temp_work_dir, 'POST')
        output_project = output_project or '.'
        if not os.path.exists(post_path):
            self.logger.info("Does not find POST script location %s", post_path)
            return

        with open(post_path, 'rb') as post:
            for post_file in post:
                post_file_path = os.path.normpath(os.path.join(output_project, post_file.strip()))
                self.logger.info("POST-generate file %s", post_file_path)
                if not os.path.exists(post_file_path):
                    self.logger.warning("POST-generate %s does not exists", post_file_path)
                    continue

                lines = open(post_file_path, 'rb').readlines()
                # convert CRLF to LF
                with open(post_file_path, 'wb') as tmp:
                    tmp.writelines([line.strip() + '\n' for line in lines])
