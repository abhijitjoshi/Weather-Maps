from rest_framework.exceptions import APIException

class GenericException(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

    def __init__(self, exception_code, detail, response=None, request=None, http_code=400):
        super(GenericException, self).__init__()
        self.status_code = http_code
        self.exception_code = exception_code
        self.detail = detail