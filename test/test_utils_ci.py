import unittest

from mock import patch

from recipe.utils import JenkinsJobForbiddenException
from recipe.utils import create_jenkins_jobs
from recipe.utils.ci import JenkinsContext
from recipe.utils.ci import Jenkins


#class JenkinsJobTestCase(unittest.TestCase):
#    @patch('recipe.utils.ci.load_project_template')
#    @patch.object(Jenkins, 'job_exists')
#    @patch.object(JenkinsContext, 'jenkins_jobs')
 #   def test_create_jenkins_job_exists(self, jenkins_jobs, job_exists, load_project_template):
#       jenkins_jobs.return_value = ['UT']
#        job_exists.return_value = True
#        load_project_template.return_value = {'python.testing': '.'}
#        self.assertRaises(JenkinsJobForbiddenException, create_jenkins_jobs, 'demo', template='python.testing')
