from __future__ import print_function

import os.path

import six

from recipe.commands.basecommand import Command
from recipe.utils import get_templates_home
from recipe.utils import load_project_template


class ListCommand(Command):
    name = 'list'

    @staticmethod
    def register(sub_parser):
        sub_parser.add_parser('list', help='list installed project templates')

    def run(self):
        templates = load_project_template(get_templates_home())
        for key, value in six.iteritems(templates):
            self.logger.debug('Process templates %s location %s', key, value)
            description = ''
            readme = os.path.join(value, 'README.md')
            if os.path.isfile(readme):
                self.logger.debug('Read %s template description in README.md', key)
                with open(readme, 'rb') as f:
                    lines = f.readlines()
                    if len(lines) >= 2:
                        description = lines[1]
            print(key, description, sep='\t\t')
