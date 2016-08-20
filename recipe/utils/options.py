import os

import configparser


class OptionParser(object):
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.files = self.get_config_file()
        if self.files:
            self.config.read(self.files)

    def get(self, section, option, default=None):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        return default

    def get_group(self, section, *fields):
        if self.config.has_section(section):
            if fields:
                return {field: self.config.get(section, field) for field in fields}
            return dict(self.config.items(section))

    def get_tuple(self, section, *fields):
        if self.config.has_section(section):
            if fields:
                return tuple(self.config.get(section, field) for field in fields)
            return tuple(self.config.get(section, field) for field in fields)

    @staticmethod
    def get_config_file():
        config_file = os.environ.get('RECIPE_CONFIG_FILE', False)
        if config_file == os.devnull:
            return None

        if os.path.exists('.reciperc'):
            return '.reciperc'

        if os.path.exists(os.path.expanduser('~/.reciperc')):
            return os.path.expanduser('~/.reciperc')

        return None
