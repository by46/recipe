from recipe.commands import Command
from recipe.hack import patch


def main():
    patch()
    cmd = Command.parse()
    cmd.execute()


if __name__ == '__main__':
    main()
