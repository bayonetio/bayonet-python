import json
from abc import ABCMeta, abstractmethod


class BayonetBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def request(self, route, arg):
        pass

    def consulting(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/consult', serialized)

    def update_transaction(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/update-transaction', serialized)

    def feedback_historical(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/feedback-historical', serialized)
    
    def blocklist_add(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/labels/block/add', serialized)
    
    def blocklist_remove(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/labels/block/remove', serialized)
    
    def whitelist_add(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/labels/whitelist/add', serialized)
    
    def whitelist_add(self, params):
        serialized = self.json_from_params(params)
        return self.request('/sigma/labels/whitelist/remove', serialized)

    def json_from_params(self, params):
        # Add api_key to params
        params['api_key'] = self.api_key
        return json.dumps(params)
