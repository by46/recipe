from recipe.commands import Command


def main():
    cmd = Command.parse()
    cmd.run()


if __name__ == '__main__':
    main()
