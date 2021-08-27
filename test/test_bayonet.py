from __future__ import print_function

import os
import sys
from types import MethodType
import unittest
import bayonet

api_key = os.environ.get('API_KEY')
if api_key is None:
    print('Set API_KEY environment variable to a valid token.',
          file=sys.stderr)
    sys.exit(1)

invalid_api_key = "da2da838-6311-4646-805f-2466954b1a11"

params_consulting = {
    "email": "test_python@bayonet.io",
    "consumer_name": "test python consumer name",
    "consumer_internal_id": "test_python_1",
    "cardholder_name": "test python cardholder name",
    "telephone": "9999999999",
    "card_number": "4111111111111111",
    "transaction_amount": 500.00,
    "currency_code": "MXN",
    "shipping_address": {
        "line_1": "test_python_line_1",
        "line_2": "test_python_line_2",
        "city": "Mexico DF",
        "state": "Mexico DF",
        "country": "MEX",
        "zip_code": "111111"
    },
    "billing_address": {
        "line_1": "test_python_line_1",
        "line_2": "test_python_line_2",
        "city": "Mexico DF",
        "state": "Mexico DF",
        "country": "MEX",
        "zip_code": "111111"
    },
    "payment_method": "card",
    "transaction_time": 1476813671,
    "order_id": "test_python_123",
    "payment_gateway": "stripe",
    "channel": "ecommerce",
    "coupon": "test_python_coupon",
    "expedited_shipping": False,
    "products": [
        {
            "product_id": "1",
            "product_name": "product_1",
            "product_price": 500.00,
            "product_category": "test"
        }
    ]
}

params_update_transaction = {
    "transaction_status": "bank_decline",
    "bayonet_tracking_id": "test_python_123"
}

params_feedback_historical = {
    "email": "test_python@bayonet.io",
    "consumer_name": "test python consumer name",
    "consumer_internal_id": "test_python_1",
    "cardholder_name": "test python cardholder name",
    "telephone": "9999999999",
    "card_number": "4111111111111111",
    "transaction_amount": 500.00,
    "currency_code": "MXN",
    "shipping_address": {
        "line_1": "test_python_line_1",
        "line_2": "test_python_line_2",
        "city": "Mexico DF",
        "state": "Mexico DF",
        "country": "MEX",
        "zip_code": "111111"
    },
    "billing_address": {
        "line_1": "test_python_line_1",
        "line_2": "test_python_line_2",
        "city": "Mexico DF",
        "state": "Mexico DF",
        "country": "MEX",
        "zip_code": "111111"
    },
    "payment_method": "card",
    "transaction_time": 1476813671,
    "order_id": "test_python_123",
    "payment_gateway": "stripe",
    "channel": "ecommerce",
    "coupon": "test_python_coupon",
    "expedited_shipping": False,
    "products": [
        {
            "product_id": "1",
            "product_name": "product_1",
            "product_price": 500.00,
            "product_category": "test"
        }
    ],
    "transaction_status": "success"
}

params_blocklist_invalid = {
    "email": "arandommailtotestxxx@xxx.com"
}

params_blocklist_valid = {
     "email": "test_python@bayonet.io"
}


class TestBayonet(unittest.TestCase):
    def setUp(self):
        self.client = bayonet.BayonetClient(api_key)

    def test_default_client_user_agent(self):
        self.assertIsNone(self.client._raw_user_agent)
        self.assertEqual(self.client._user_agent,
                         "OfficialBayonetPythonSDK")

    def test_default_api_hostname(self):
        self.assertEqual(self.client._api_hostname, 'api.bayonet.io')

    def test_client_api_version_namespace(self):
        self.assertEqual(self.client._api_version_namespace, 'v2')

    def test_fully_qualified_api_host_name(self):
        self.assertEqual(self.client.fully_qualified_api_hostname(),
                         'https://api.bayonet.io/v2')

    def test_client_must_respond_to__request(self):
        assert type(self.client.request) is MethodType


class TestConsult(unittest.TestCase):
    def setUp(self):
        self.client = bayonet.BayonetClient(api_key)
        self.invalid_client = bayonet.BayonetClient(invalid_api_key)

    def test_should_return_error_on_invalid_api_key(self):
        with self.assertRaises(bayonet.BayonetError):
            self.invalid_client.consulting(params_consulting)

    def test_should_validate_api_key(self):
        try:
            self.invalid_client.consulting(params_consulting)
        except bayonet.BayonetError as e:
            self.assertEqual(e.reason_code, 12)

    def test_should_return_success(self):
        r = self.client.consulting(params_consulting)
        global bayonet_tracking_id
        bayonet_tracking_id = r.bayonet_tracking_id
        self.assertEqual(r.reason_code, 0)

    def test_should_return_bayonet_tracking_id(self):
        r = self.client.consulting(params_consulting)
        assert r.bayonet_tracking_id is not None


class TestUpdateTransaction(unittest.TestCase):
    def setUp(self):
        self.client = bayonet.BayonetClient(api_key)
        self.invalid_client = bayonet.BayonetClient(invalid_api_key)

    def test_should_validate_api_key(self):
        try:
            self.invalid_client.update_transaction(params_update_transaction)
        except bayonet.BayonetError as e:
            self.assertEqual(e.reason_code, 12)

    def test_should_return_error_on_invalid_bayonet_tracking_code(self):
        params_update_transaction['bayonet_tracking_id'] = 'xxx'
        with self.assertRaises(bayonet.BayonetError):
            self.client.update_transaction(params_update_transaction)

    def test_should_validate_bayonet_tracking_id(self):
        params_update_transaction['bayonet_tracking_id'] = 'xxx'
        try:
            self.client.update_transaction(params_update_transaction)
        except bayonet.BayonetError as e:
            self.assertEqual(e.reason_code, 162)

    def test_should_return_success(self):
        params_update_transaction['bayonet_tracking_id'] = bayonet_tracking_id
        r = self.client.update_transaction(params_update_transaction)
        self.assertEqual(r.reason_code, 0)


class TestFeedbackHistorical(unittest.TestCase):
    def setUp(self):
        self.client = bayonet.BayonetClient(api_key)
        self.invalid_client = bayonet.BayonetClient(invalid_api_key)

    def test_should_validate_api_key(self):
        try:
            self.invalid_client.feedback_historical(params_feedback_historical)
        except bayonet.BayonetError as e:
            self.assertEqual(e.reason_code, 12)

    def test_should_return_success(self):
        r = self.client.feedback_historical(params_feedback_historical)
        self.assertEqual(r.reason_code, 0)

if __name__ == "__main__":
    unittest.main()
