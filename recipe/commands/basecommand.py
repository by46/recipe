import argparse
import getpass
import logging
import socket
import sys
from datetime import datetime

from simplekit import email

from recipe.utils import OptionParser
from recipe.utils import RecipeRuntimeException
from recipe.utils import config_logging

EMAIL_API = 'http://10.16.75.24:3000/framework/v1/mail'


class Command(object):
    """this is the base class for all commands

    """
    name = None
    SNAP = {}
    parser = argparse.ArgumentParser(description='recipe')

    def __init__(self, options):
        self.options = options
        config_logging(options)
        self.config = OptionParser()
        email.settings.URL_EMAIL = self.config.get('email', 'api', EMAIL_API)
        self.logger = logging.getLogger('recipe')

    @staticmethod
    def register(cmd_class=None):
        """register the command

        :param cmd_class: `class`:`str`
        :return:
        """
        if cmd_class is None:
            parser = Command.parser = argparse.ArgumentParser(description='recipe')
            parser.add_argument('--verbose', '-v', action='count', default=2,
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
        """ run this command

        :return:
        """
        raise NotImplementedError

    def execute(self):
        try:
            self.run()
        except RecipeRuntimeException:
            raise
        except Exception as e:
            self.logger.exception(e)
            # send email
            sender = 'Recipe@newegg.com'
            receiver = self.config.get('email', 'receiver', 'benjamin.c.yan@newegg.com')
            cc = self.config.get('email', 'cc')
            subject = "(Info) Recipe Error"
            body = "Hi, \n Recipe occur unknown error with login {0} on {1} at {2}".format(getpass.getuser(),
                                                                                           socket.gethostname(),
                                                                                           datetime.now().strftime(
                                                                                               '%a %b %d %H:%M:%S %Y'))
            email.send_email(sender, receiver, subject, body, cc=cc, files=[self.options.log])
            raise RecipeRuntimeException(3)
