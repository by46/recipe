from basecommand import Command
from project import ProjectCommand

Command.register()
Command.register(ProjectCommand)
