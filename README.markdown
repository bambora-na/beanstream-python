## Bambora Python API

The goal of this library is to provide a python implementation of the
Beanstream API.

The library supports:

 * payment profiles
 * one off transactions
 * pre-authorizing transactions
 * voiding transactions
 * recurring billing
 * reporting

The library is licensed under the Apache 2.0 license
(http://www.apache.org/licenses/LICENSE-2.0).

## Install
When you have checked out this code using Git, you then just have to navigate to the root SDK source code directory and run:
    python setup.py install

## TLS 1.2 support
For testing instructions with our TLS1.2-only server, please refer to our [developer portal](https://dev.na.bambora.com/docs/references/payment_SDKs/support_tls12/#python-sdk)

## Getting started

The API is interacted with through the Gateway object. The Gateway holds all of
the beanstream account configuration.

    from beanstream import gateway
    beangw = gateway.Beanstream(
        True, #require billing address
        True) #require CVD code
    beangw.configure(
        YOUR_MERCHANT_ID,
        YOUR_PAYMENT_API_PASSCODE,
		YOUR_PROFILES_API_PASSCODE,
		YOUR_RECURRING_BILLING_API_PASSCODE,
		YOUR_REPORTING_API_PASSCODE)

The `gateway` object has methods for constructing `transaction`s to the
Beanstream API. A `transaction` encapsulates the information involved in a
request against the beanstream API.

Ex. Making a one off credit card transaction:

    from beanstream import gateway, billing
    
    beangw = create_gateway()
    card = billing.CreditCard(
        'John Doe',
        '4030000010001234',
        '09', '2015',
        '123')
    
    txn = beangw.purchase(50, card, self.billing_address)
    txn.set_comments('$50 Frobinator for John Doe')
    resp = txn.commit()
    
    if resp.approved():
        ship_frobinator('John Doe')


## Running tests

Run the command `nosetests test.py`.

The tests attempt to make requests against the Beanstream API using the test
credit cards given for sandbox use.

This project comes with the API keys for a Beanstream test account that you can use if you haven't created your own yet.

Example config file:

    # these are values for the sample test account
    [rules]
    require_billing_address: false
    require_cvd: true

    [beanstream]
    merchant_id: 300200578
    payment_passcode: 4BaD82D9197b4cc4b70a221911eE9f70
    payment_profile_passcode: D97D3BE1EE964A6193D17A571D9FBC80
    reporting_passcode: 4e6Ff318bee64EA391609de89aD4CF5d
    recurring_billing_passcode=D5A56B15F58d404681aC1DE1C3fE80c4

## Example Code
To see working examples of payments, recurring billing, payment profiles, and reporting, take a look at test.py
