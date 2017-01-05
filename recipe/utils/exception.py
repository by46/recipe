class RecipeError(Exception):
    """Recipe Base exception

    """


class JenkinsException(RecipeError):
    """Jenkins job relative exception

    """


class JenkinsJobForbiddenException(JenkinsException):
    """Jenkins job already exists

    """

    def __init__(self, job_name):
        self.job_name = job_name
        message = "Jenkins job {0} already exists, create this job is forbidden.".format(job_name)
        super(JenkinsJobForbiddenException, self).__init__(message)


class JenkinsViewForbiddenExceptioin(JenkinsException):
    """Jenkins views already exists
    
    """

    def __init__(self, view_name):
        self.view_name = view_name
        message = "Jenkins view {0} already exists, create this views is forbidden".format(view_name)
        super(JenkinsViewForbiddenExceptioin, self).__init__(message)


class RecipeRuntimeException(RecipeError):
    """Recipe Base exception

    """

    def __init__(self, exit_code=1):
        msg = 'Recipe Runtime exception, exit code {0}'.format(exit_code)
        super(RecipeRuntimeException, self).__init__(msg)
        self.exit_code = exit_code

class CloudDataException(RecipeError):
    """Call Cloud Data Exception

    """

    def __init__(self, cloud_data,body):
        msg = 'Cloud Data exception, {0} {1}'.format(cloud_data, body)
        super(CloudDataException, self).__init__(msg)
        self.cloud_data = cloud_data