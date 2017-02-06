'''
Copyright 2012 Upverter Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from __future__ import unicode_literals

import decimal
import hashlib
import logging
import random
import string
import base64
import urllib
import time
import json

from beanstream import errors
from beanstream.compat import get_status, HTTPSConnection, urlencode, Request, open_url, parse_qs
from beanstream.response_codes import response_codes

log = logging.getLogger('beanstream.transaction')


class Transaction(object):

    URLS = {
        'process_transaction'   : '/scripts/process_transaction.asp',
        'recurring_billing'     : '/scripts/recurring_billing.asp',
        'payment_profile'       : '/scripts/payment_profile.asp',
        'report_download'       : '/scripts/report_download.asp',
        'report'                : '/scripts/report.aspx',
        'rest_payments'         : '/api/v1/payments',
        'rest_reports'          : '/api/v1/reports',
        'rest_profiles'         : '/api/v1/profiles'
    }

    TRN_TYPES = {
        'preauth': 'PA',
        'preauth_completion': 'PAC',
        'purchase': 'P',
        'return': 'R',
        'void': 'V',
        'void_purchase': 'VP',
        'void_return': 'VR',
    }


    def __init__(self, beanstream):
        self.beanstream = beanstream
        self.response_class = Response

        self.restful = False

        self.params = {}

        self._generate_order_number()
        self.params['trnOrderNumber'] = self.order_number
        self.response_params = []
        self.request_type = None

    def validate(self):
        pass

    def commit(self):
        self.validate()

        '''
        # hashing is applicable only to requests sent to the process
        # transaction API.
        if self.restful:
            self.generate_rest_json()
            data = self.params['rest']
            #print("================ sending json:")
            #print(data)
        else:
            data = urlencode(self.params)
        '''

        # do switch statement for which passcode to use
        apicode = None
        if (self.url == self.URLS['process_transaction']):
            apicode = self.beanstream.payment_passcode
        elif (self.url == self.URLS['recurring_billing']):
            apicode = self.beanstream.recurring_billing_passcode
        elif (self.url == self.URLS['payment_profile']):
            apicode = self.beanstream.payment_profile_passcode
        elif (self.url == self.URLS['rest_payments']):
            apicode = self.beanstream.payment_passcode
        elif (self.url == self.URLS['rest_profiles']):
            apicode = self.beanstream.payment_profile_passcode
        else:
            apicode = self.beanstream.reporting_passcode

        if (apicode is None):
            log.error('No API Passcode specified for url %s', self.url)
            return False



        auth = base64.b64encode( (str(self.beanstream.merchant_id)+':'+apicode).encode('utf-8') )
        passcode = 'Passcode '+str(auth.decode('utf-8'))

        #for testing exception handling
        if self.beanstream.testErrorGenerator is not None:
            return self.beanstream.testErrorGenerator.generateError()


        if self.restful:
            return self.process_rest(passcode)           #REST API
        else:
            return self.process_query_param(passcode)    #Classic QueryParam API


    def handle_errors(self, response):
        #non-OK response occured, return error
        status = get_status(response)
        if status != 200:
            message = response.read()
            message = message.decode('utf-8')
            log.error('response code not OK: %s message: ', status, message)
            return errors.getMappedException(status)
        else:
            return None

    '''
    Submit and process requests to the REST API.
    '''
    def process_rest(self, passcode):
        self.generate_rest_json()
        data = self.params['rest']

        self.populate_url()
        log.debug('Sending to %s: %s', self.url, data)
        '''print('Sending to ', 'https://www.beanstream.com'+self.url, data)'''

        requestType = self.request_type
        if requestType is None:
            if data is None:
                requestType = 'GET'
            else:
                requestType = 'POST'
        headers={
            'Content-Type': 'application/json',
            'Authorization': passcode
        }
        connection = HTTPSConnection('www.beanstream.com')
        try:
            connection.request(requestType, self.url, data, headers)
            response = connection.getresponse()

            errors = self.handle_errors(response)
            if errors is not None:
                return errors

            body = response.read()
            body = body.decode('utf-8')

            return json.loads(body)
        finally:
            connection.close()


    '''
    Submit and process requests to the QueryString API.
    '''
    def process_query_param(self, passcode):
        data = urlencode(self.params)

        '''print('Sending to ', 'https://www.beanstream.com'+self.url, data)'''
        
        log.debug('Sending to %s: %s', self.url, data)
        request = Request('https://www.beanstream.com'+self.url)
        request.add_header('Authorization', passcode)

        res = open_url(request, data)

        errors = self.handle_errors(res)
        if errors is not None:
            return errors

        body = res.read()
        body = body.decode('utf-8')

        response = self.parse_raw_response(body)
        log.debug('Beanstream response: %s', body)
        log.debug(response)

        return self.response_class(response, *self.response_params)


    ''' Overwrite in Restful subclasses'''
    def generateRestJson(self):
        pass

    ''' Overwrite in Restful subclasses'''
    def populate_url(self):
        pass

    def parse_raw_response(self, body):
        return parse_qs(body)

    def _generate_order_number(self):
        """ Generate a random 10-digit alphanumeric string prefixed with a timestamp.
        """
        t = str(time.time())
        n = str(random.randint(0, 1000))
        self.order_number = t+n

    def _process_amount(self, amount):
        decimal_amount = decimal.Decimal(amount)
        return str(decimal_amount.quantize(decimal.Decimal('1.00')))

    def set_card(self, card):
        if self.beanstream.REQUIRE_CVD and not card.has_cvd():
            log.error('CVD required')
            raise errors.ValidationException('CVD required')

        self.params.update(card.params())
        self.has_credit_card = True

    def set_billing_address(self, address):
        self.params.update(address.params('ord'))
        self.has_billing_address = True

    def set_refs(self, refs):
        if len(refs) > 5:
            raise errors.ValidationException('too many ref fields')

        for ref_idx, ref in enumerate(refs, start=1):
            if ref:
                self.params['ref%s' % ref_idx] = ref


'''
    Optional response object wrapper used by non-restful request responses.
'''
class Response(object):

    def __init__(self, resp_dict):
        self.resp = resp_dict

    def __repr__(self):
        return '%s(%s)' % (self.__class__, self.resp)

    def __str__(self):
        return '%s <transaction_id: %s, order_number: %s>' % (self.__class__, self.transaction_id(), self.order_number())

    def order_number(self):
        ''' Order number assigned in the transaction request. '''
        return self.resp.get('trnOrderNumber', [None])[0]

    def transaction_id(self):
        ''' Beanstream transaction identifier '''
        return self.resp.get('trnId', [None])[0]

    def refs(self):
        return [
            self.resp.get('ref1', [None])[0],
            self.resp.get('ref2', [None])[0],
            self.resp.get('ref3', [None])[0],
            self.resp.get('ref4', [None])[0],
            self.resp.get('ref5', [None])[0],
        ]

