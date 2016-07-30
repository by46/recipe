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
        print (('package_name:' + 'recipe'),
               ('recipe_version:' + recipe.__version__),
               ('from:' + package_dir()))
