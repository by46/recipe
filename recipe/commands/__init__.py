from basecommand import Command
from listcommand import ListCommand
from project import ProjectCommand

Command.register()
Command.register(ProjectCommand)
Command.register(ListCommand)
