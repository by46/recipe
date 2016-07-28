import argparse
import logging
import os
import shutil
import sys
import tempfile

from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter

from ci import create_jenkins_jobs
from template import gen_cookie_cutter_meta_json
from template import load_project_template
from utils import config_logging
from utils import get_templates_home
from utils import valid_project_slug


def main():
    parser = argparse.ArgumentParser(description="recipe tools")
    parser.add_argument('-t', '--template', dest='template', default='python.flask', help="project template name")
    parser.add_argument('-o', '--output-dir', dest='out', default='.',
                        help='Where to output the generated project dir into')
    parser.add_argument('--verbose', '-v', action='count', default=1)
    parser.add_argument('-r', '--repo', dest='repo',
                        help='the git repo on trgit2, like: https://trgit2/dfis/recipe.git')
    parser.add_argument('name')
    args = parser.parse_args()

    # config logger
    config_logging(args)
    logger = logging.getLogger('recipe')

    project_slug = args.name

    # check project name
    if not valid_project_slug(project_slug):
        logger.critical('Project name is invalid, just contain alpha, digit, underscore(_), and max length is 50.')

    templates_home = get_templates_home()
    if templates_home is None:
        logger.critical('Checking project templates does not exists')

    logger.info('Loading project templates from %s', templates_home)
    templates = load_project_template(templates_home)

    if args.template not in templates:
        logger.error('%s does not exists', args.template)
        sys.exit(1)

    temp_work_dir = tempfile.mkdtemp(prefix='recipe-{0}-'.format(project_slug))
    os.rmdir(temp_work_dir)
    shutil.copytree(templates[args.template], temp_work_dir)
    logger.info('Copying project templates into %s', temp_work_dir)

    if not os.path.isdir(args.out):
        logger.info('Creating output dir %s', args.out)
        os.makedirs(args.out)

    try:
        gen_cookie_cutter_meta_json(temp_work_dir, project_slug)
        cookiecutter(temp_work_dir, no_input=True, output_dir=args.out)

        create_jenkins_jobs(project_slug, args.repo)

    except OutputDirExistsException as e:
        logger.warning("%s directory already exists, please ensure it does not exists. ",
                       os.path.join(args.out, project_slug))
        sys.exit(2)
    except Exception as e:
        logger.exception(e)
        sys.exit(3)


if __name__ == '__main__':
    main()
