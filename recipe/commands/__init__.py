from basecommand import Command
from listcommand import ListCommand
from project import ProjectCommand
from version import VersionCommand

Command.register()
Command.register(ProjectCommand)
Command.register(ListCommand)
Command.register(VersionCommand)
