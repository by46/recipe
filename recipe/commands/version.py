from recipe.commands import Command
import recipe


class VersionCommand(Command):
    name = "version"

    def __init__(self, options):
        super(VersionCommand, self).__init__(options)

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('version', help='version help')

    def run(self):
        print (recipe.__version__)
