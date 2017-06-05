import json


class BayonetError(Exception):
    """All errors related to making an API request extend this."""

    def __init__(self, message=None,
                 request_body=None, request_headers=None,
                 http_response_code=None, http_response_message=None):
        super(BayonetError, self).__init__(message)

        self.request_body = request_body
        self.request_headers = request_headers
        self.http_response_code = http_response_code
        self.http_response_message = http_response_message

        # Get reason_code and reason_message from response
        try:
            response_as_json = json.loads(http_response_message)
            if 'reason_code' in response_as_json:
                self.reason_code = response_as_json['reason_code']
            else:
                self.reason_code = None
            if 'reason_message' in response_as_json:
                self.reason_message = response_as_json['reason_message']
            else:
                self.reason_message = None
            if 'status' in response_as_json:
                self.status = response_as_json['status']
            else:
                self.status = None
        except ValueError:
            self.reason_code = None
            self.reason_message = None
            self.status = None


class InvalidClientSetupError(Exception):
    def __init__(self, message=None):
        super(InvalidClientSetupError, self).__init__(message)
