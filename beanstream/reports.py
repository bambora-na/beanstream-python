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

import logging
import re
import json
from enum import Enum

from beanstream import billing, errors, transaction

log = logging.getLogger('beanstream.reports')

class Report(transaction.Transaction):

    def __init__(self, beanstream):
        super(Report, self).__init__(beanstream)
        self.url = self.URLS['rest_reports']
        self.response_class = ReportResponse

        self.params['merchantId'] = self.beanstream.merchant_id
        self.params['passCode'] = self.beanstream.reporting_passcode

        self.restful = True #we send RESTful requests for reports and to get payments

    def use_payments_api(self):
        self.url = self.URLS['rest_payments']

    def use_reports_api(self):
        self.url = self.URLS['rest_reports']

    def parse_raw_response(self, body):
        pass
        


class ReportResponse(transaction.Response):

    @classmethod
    def _fields(cls):
        return []

    def items(self):
        return self.resp

class GetTransaction(Report):
    def __init__(self, beanstream):
        super(GetTransaction, self).__init__(beanstream)
        self.request_type = 'GET'
        
    def generate_rest_json(self):
        self.params['rest'] = None

    def set_transaction_id(self, transId):
        self.params['transId'] = transId

    def populate_url(self):
        #add the transaction id to the url
        self.url = self.url+'/'+str(self.params['transId'])
    
    
class TransactionReport(Report):

    def __init__(self, beanstream):
        super(TransactionReport, self).__init__(beanstream)
        self.request_type = 'POST'


    def generate_rest_json(self):
        self.params['rest'] = json.dumps({
            'name': 'Search',
            'start_date': self.params['startDate'],
            'end_date': self.params['endDate'],
            'start_row': self.params['startRow'],
            'end_row': self.params['endRow'],
            'criteria':self.params['criteria']
        })
        
    def set_query_params(self, startDate, endDate, startRow=0, endRow=100, criteriaList=None):
        self.params['startDate'] = str(startDate.strftime('%Y-%m-%dT%H:%M:%S'))
        self.params['endDate'] = str(endDate.strftime('%Y-%m-%dT%H:%M:%S')) # eg. 2015-06-05T16:05:00
        self.params['startRow'] = startRow
        self.params['endRow'] = endRow
        if criteriaList is not None:
            crit = []
            for c in criteriaList:
                crit.append({
                    'field': c.field,
                    'operator': c.operator,
                    'value': c.value
                })
            self.params['criteria'] = crit
        else:
            self.params['criteria'] = None

    def populate_url(self):
        pass #we don't modify this url



''' search criteria:
    "field": "1",    (pass in a reports.Fields object)
    "operator": "%3C%3D",
    "value": "10000001"
'''
class Criteria(object):
    def __init__(self, field, operator, value):
        self.field = field.value
        self.operator = operator.toStr()
        self.value = value

class Operator(object):
    def __init__(self, val):
        self.value = val
        
    def toStr(self):
        if self.value == '=':
            return '%3D'
        elif self.value == '<':
            return '%3C'
        elif self.value == '>':
            return '%3E'
        elif self.value == '<=':
            return '%3C%3D'
        elif self.value == '>=':
            return '%3E%3D'
        elif self.value == 'START WITH':
            return 'START%20WITH'
        else:
            return errors.ValidationException("Unrecognized Operator parameter for report query: "+value)

class Fields(Enum):
    TransactionId = 1      # >=,<=,=,<>,>,<
    Amount = 2             # >=,<=,=,<>,>,<
    MaskedCardNumber = 3   # =
    CardOwner = 4          # =,START WITH
    OrderNumber = 5        # >=,<=,=,<>,>,<
    IPAddress = 6          # =,START WITH
    AuthorizationCode = 7  # =,START WITH
    TransType = 8          # =
    CardType = 9           # =
    Response = 10          # =
    BillingName = 11       # =,START WITH
    BillingEmail = 12      # =,START WITH
    BillingPhone = 13      # =,START WITH
    ProcessedBy = 14       # =
    Ref1 = 15              # =,START WITH
    Ref2 = 16              # =,START WITH
    Ref3 = 17              # =,START WITH
    Ref4 = 18              # =,START WITH
    Ref5 = 19              # =,START WITH
    ProductName = 20       # =,START WITH
    ProductID = 21         # =,START WITH
    CustCode = 22          # =,START WITH
    IDAdjustmentTo = 23    # =
    IDAdjustedBy = 24      # =
