from __future__ import print_function

import recipe
from recipe.commands import Command
from recipe.utils import package_dir


class VersionCommand(Command):
    name = "version"

    @staticmethod
    def register(sub_parser):
        sub_parser.add_parser('version', help='version help')

    def run(self):
        print('recipe',
              recipe.__version__,
              'from:' + package_dir(), sep=' ')
