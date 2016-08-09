from .basecommand import Command
from .deploycommand import DeployCommand
from .install import InstallCommand
from .listcommand import ListCommand
from .project import ProjectCommand
from .version import VersionCommand

Command.register()
Command.register(ProjectCommand)
Command.register(ListCommand)
Command.register(VersionCommand)
Command.register(DeployCommand)
Command.register(InstallCommand)
