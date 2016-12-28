from recipe.commands import Command
from recipe.hack import patch
import sys
from recipe.utils import RecipeRuntimeException
from cookiecutter.exceptions import OutputDirExistsException


def main():
    patch()
    try:
        cmd = Command.parse()
        cmd.execute()
    except RecipeRuntimeException as e:
        sys.exit(e.exit_code)


if __name__ == '__main__':
    main()
