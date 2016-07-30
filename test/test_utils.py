import unittest

from recipe import utils


class UtilTestCase(unittest.TestCase):
    def test_valid_project_slug(self):
        project_slug = "Recipe0123456789_mock"
        self.assertTrue(utils.valid_project_slug(project_slug))

        project_slug = 'Recipe00000000000000000000000000000000000000000000'
        self.assertTrue(utils.valid_project_slug(project_slug))

        project_slug = ""
        self.assertFalse(utils.valid_project_slug(project_slug))

        project_slug = "Recipe000000000000000000000000000000000000000000001"
        self.assertFalse(utils.valid_project_slug(project_slug))

        project_slug = "-!@#$%^&*()_+"
        self.assertFalse(utils.valid_project_slug(project_slug))
