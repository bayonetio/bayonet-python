import json


class BayonetResponse(object):
    def __init__(self, response):
        parsed_response = json.loads(response.content)
        if 'bayonet_tracking_id' in parsed_response:
            self.bayonet_tracking_id = parsed_response['bayonet_tracking_id']
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
        self.raw = parsed_response
