## Bayonet
Bayonet enables companies to feed and consult a global database about online consumers’ reputation, based on historic payments. Start making smarter business decisions today.

### Introduction
Bayonet’s API is organized around REST and exposes endpoints for HTTP requests. It is designed to have predictable, resource-oriented URLs and uses standard HTTP response codes to indicate the outcome of operations. Request and response payloads are formatted as JSON.

### About the service
Bayonet provides an Ecosystem of Trust and Protection where companies can colaborate with each other to combat online fraud together. We provide a secure platform to share and consult data to understand when a consumer is related to fraudulent activity or has a fraud-free record. Different technologies that run algorithms to link parameters seen in different transactions, fed by companies connected to the ecosystem are employed in order to build consumer profiles. By consulting Bayonet’s API, a response with data provided by companies themselves is available in real-time for your risk assesment process to analyze it and take better decisions.

### Bayonet's API details
To know more about Bayonet's API and its domain and technical details, please see the "Integration Specs V 1.0" document provided by the Bayonet team.

## Getting started
To use this SDK, please make sure:
  * You have Python 2.7 or superior installed on your system.
  * Your system supports TLS v1.2.
  * You have an API KEY (sandbox and/or live) provided by Bayonet's team.
  * Install the 'bayonet' package on your system
  
    ```sh
    pip install --upgrade bayonet
    ```
    or using easy_install:
    
    ```sh
    easy_install --upgrade bayonet
    ```
    If you're not using virtualenv, you may have to prefix those commands with `sudo`.
    
    You can also install from source:
    
    ```sh
    python setup.py install
    ```
  * Import 'bayonet' in your file

    ```py
    import bayonet
    ```
  * Create config options, with parameters (api_key, api_version).

    ```py
    client = bayonet.BayonetClient(api_key, api_version)
    ```
    
## Usage
Once you have Bayonet's SDK configured, you can call the three APIs with the following syntax:
  * Consulting API
  
    ```py
    client.consulting({
        "channel": "mpos",
        "email": "example@bayonet.io",
        "consumer_name": "Example name",
        "cardholder_name": "Example name",
        "payment_method": "card",
        "card_number": 4111111111111111,
        "transaction_amount": 999,
        "currency_code": "MXN",
        "transaction_time": 1476012879,
        "coupon": False,
        "payment_gateway": "stripe",
        "shipping_address" : {
            "address_line_1" : "example line 1",
            "address_line_2" : "example line 2",
            "city" : "Mexico City",
            "state" : "Mexico DF",
            "country" : "MEX",
            "zip_code" : "64000"
        }
    })
    ```
  * Feedback API
  
    ```py
    client.feedback({
        "transaction_status": "success",
        "transaction_id": "uhffytd65rds56yt",
        ...
    })
    ```
  * Feedback-historical API
  
    ```py
    client.feedback_historical({
        "channel": "mpos",
        "type": "transaction",
        "email": "example@bayonet.io",
        "consumer_name": "Example name",
        "payment_method": "card",
        "card_number": 4111111111111111,
        "transaction_amount": 999,
        "currency_code": "MXN",
        "transaction_time": 1423823404,
        "transaction_status": "bank_decline",
        "transaction_id": "uhffytd65rds56yt",
        "coupon": False,
        "payment_gateway": "stripe",
        "device_fingerprint": "AF567GHGJJJ87JH",
        "bank_auth_code": "5353888",
        "telephone": "0000000000",
        "expedited_shipping": False,
        "bank_decline_reason": "stolen_card",
        "shipping_address": {
            "address_line_1": "example line 1",
            "address_line_2": "example line 2",
            "city": "Mexico City",
            "state": "Mexico DF",
            "country": "MEX",
            "zip_code": "64000"
        }
    })
    ```
 
## Error handling
Bayonet's SDK raises exceptions both when setting up the client object and executing functions:
```py
try:
    client = bayonet.BayonetClient(api_key, api_version)
except bayonet.exceptions.InvalidClientSetupError as e:
    print (e.message)
```

```py
try:
    client.consulting(params)   # Or, client.feedback(params) Or, client.feedback_historical(params)
except bayonet.exceptions.BayonetError as e:
    print (e.reason_code)
    print (e.reason_message)
```

For a full list of error codes and their messages, please refer to the Bayonet API documentation.

## Testing
You can run the test suite with the following command:
```sh
python setup.py test
```
