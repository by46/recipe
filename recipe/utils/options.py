import os

import configparser


class OptionParser(object):
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.files = self.get_config_files()
        if self.files:
            self.config.read(self.files)

    def get(self, section, option):
        return self.config.get(section, option)

    @staticmethod
    def get_config_files():
        config_file = os.environ.get('RECIPE_CONFIG_FILE', False)
        if config_file == os.devnull:
            return []

        return [os.path.expanduser('~/.reciperc'), '.reciperc']
