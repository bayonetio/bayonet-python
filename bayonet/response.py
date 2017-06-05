import json


class BayonetResponse(object):
    def __init__(self, response):
        parsed_response = json.loads(response.content)
        if 'feedback_api_trans_code' in parsed_response:
            self.feedback_api_trans_code = parsed_response['feedback_api_trans_code']
        else:
            self.feedback_api_trans_code = None
        if 'rules_triggered' in parsed_response:
            self.rules_triggered = parsed_response['rules_triggered']
        else:
            self.rules_triggered = None
        if 'risk_level' in parsed_response:
            self.risk_level = parsed_response['risk_level']
        else:
            self.risk_level = None
        if 'payload' in parsed_response:
            self.payload = parsed_response['payload']
        else:
            self.payload = None
        if 'reason_code' in parsed_response:
            self.reason_code = parsed_response['reason_code']
        else:
            self.reason_code = None
        if 'reason_message' in parsed_response:
            self.reason_message = parsed_response['reason_message']
        else:
            self.reason_message = None
        if 'request_body' in parsed_response:
            self.request_body = parsed_response['request_body']
        else:
            self.request_body = None
        if 'bayonet_fingerprint' in parsed_response:
            self.bayonet_fingerprint = parsed_response['bayonet_fingerprint']
        else:
            self.bayonet_fingerprint = None
        self.raw = parsed_response
