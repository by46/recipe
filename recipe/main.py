from cookiecutter.main import cookiecutter


def main():
    cookiecutter('../templates/python.flask', no_input=True)


if __name__ == '__main__':
    main()
