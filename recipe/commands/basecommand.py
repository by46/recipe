import argparse
import logging
import sys

from recipe.utils import config_logging


class Command(object):
    name = None
    usage = None
    cmds = {}
    parser = argparse.ArgumentParser(description='recipe')

    def __init__(self, options):
        self.options = options
        config_logging(options)
        self.logger = logging.getLogger('recipe')
        # TODO(benjamin): init logger

    @staticmethod
    def register(cmd_class=None):
        if cmd_class is None:
            parser = Command.parser = argparse.ArgumentParser(description='recipe')
            parser.add_argument('--verbose', '-v', action='count', default=1)
            Command.sub_parser = parser.add_subparsers(help='sub-command help', dest='command')
        else:
            if cmd_class.name not in Command.cmds:
                cmd_class.register(Command.sub_parser)
                Command.cmds[cmd_class.name] = cmd_class

    @staticmethod
    def parse(args=None):
        if args is None:
            args = sys.argv[1:]
        parser = Command.parser
        options = parser.parse_args(args)
        cmd = options.command
        if cmd in Command.cmds:
            return Command.cmds[cmd](options)

    def run(self):
        pass
