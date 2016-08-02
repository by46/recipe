import argparse
import logging
import sys

from recipe.utils import OptionParser
from recipe.utils import config_logging


class Command(object):
    name = None
    SNAP = {}
    parser = argparse.ArgumentParser(description='recipe')

    def __init__(self, options):
        self.options = options
        config_logging(options)
        self.config = OptionParser()
        self.logger = logging.getLogger('recipe')

    @staticmethod
    def register(cmd_class=None):
        if cmd_class is None:
            parser = Command.parser = argparse.ArgumentParser(description='recipe')
            parser.add_argument('--verbose', '-v', action='count', default=1,
                                help='Give more output, Options is additive, and can be used up to 3 times.')
            parser.add_argument('--log', dest='log', default=None, help='Path to a verbose appending log')
            Command.sub_parser = parser.add_subparsers(help='Available commands', dest='command')
        else:
            if cmd_class.name not in Command.SNAP:
                cmd_class.register(Command.sub_parser)
                Command.SNAP[cmd_class.name] = cmd_class

    @staticmethod
    def parse(args=None):
        if args is None:
            args = sys.argv[1:]
        parser = Command.parser
        options = parser.parse_args(args)
        cmd = options.command
        if cmd in Command.SNAP:
            return Command.SNAP[cmd](options)

    def run(self):
        raise NotImplementedError
