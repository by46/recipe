from __future__ import print_function
from recipe.commands import Command
import recipe
from recipe.utils import package_dir


class VersionCommand(Command):
    name = "version"

    def __init__(self, options):
        super(VersionCommand, self).__init__(options)

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('version', help='version help')

    def run(self):
        print('recipe',
              recipe.__version__,
              'from:' + package_dir(), sep=' ')
