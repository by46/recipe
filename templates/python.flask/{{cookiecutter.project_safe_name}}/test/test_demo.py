import unittest

import app
from app import create_app


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app('test').test_client()

    def test_hello_world(self):
        response = self.client.get('/{{cookiecutter.project_slug}}', follow_redirects=True)
        self.assertTrue('The Art of Computer Programming' in response.data)

    def test_version(self):
        response = self.client.get('/{{cookiecutter.project_slug}}/version', follow_redirects=True)
        self.assertTrue(app.__version__ in response.data)

    def test_faq(self):
        response = self.client.get('/{{cookiecutter.project_slug}}/faq.htm')
        self.assertEqual('<!--Newegg-->', response.data)
