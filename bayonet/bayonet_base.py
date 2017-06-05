import json
from abc import ABCMeta, abstractmethod


class BayonetBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, api_key, version):
        self.api_key = api_key
        self.version = version

    @abstractmethod
    def request(self, route, arg):
        pass

    def consulting(self, params):
        serialized = self.json_from_params(params)
        return self.request('/consulting', serialized)

    def feedback(self, params):
        serialized = self.json_from_params(params)
        return self.request('/feedback', serialized)

    def feedback_historical(self, params):
        serialized = self.json_from_params(params)
        return self.request('/feedback-historical', serialized)

    def get_fingerprint_data(self, params):
        serialized = self.json_from_params(params)
        return self.request('/get-fingerprint-data', serialized)

    def json_from_params(self, params):
        # Add api_key to params
        params['api_key'] = self.api_key
        return json.dumps(params)
