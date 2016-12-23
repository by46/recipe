from recipe.commands import Command

if __name__ == '__main__':
    name = "demo7"
    Command.parse(["create", '-o', "D:\\tmp\\template_project", "--init-repo", name]).execute()
