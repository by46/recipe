from recipe.commands import Command


class InstallCommand(Command):
    name = 'install'

    @staticmethod
    def register(sub_parser):
        parser = sub_parser.add_parser('install', help='Install extra project templates.')

    def run(self):
        pass
