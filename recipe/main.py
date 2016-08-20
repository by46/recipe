from recipe.commands import Command


def main():
    cmd = Command.parse()
    cmd.execute()


if __name__ == '__main__':
    main()
