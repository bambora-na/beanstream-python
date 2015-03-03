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

class Error(Exception):
    pass

# define a superclass BeanstreamApiException
# Author: Haggai Liu

class BeanstreamApiException(Error):
   pass

class ConfigurationException(BeanstreamApiException):
    pass

class ValidationException(BeanstreamApiException): #parameters to a request were incorrect
    pass

class RedirectionException(BeanstreamApiException):#HTTP status code 302
    pass

class InvalidRequestException(BeanstreamApiException):#HTTP status code 400,405,415
    pass

class UnAuthorizedException(BeanstreamApiException):#HTTP status code 401
    pass

class BusinessRuleException(BeanstreamApiException):#HTTP status code 402
    pass

class ForbiddenException(BeanstreamApiException):#HTTP status code 403
    pass
 
class InternalServerException(BeanstreamApiException):#default
   pass


def getMappedException(httpstatuscode):
   code=str(httpstatuscode)
   if code=='302':
      return RedirectionException
   if code[0]=='4':
      code=code[1:]
      if code in ['00','05','15']:
         return InvalidRequestException
      if code[0]=='0':
         code=code[1:]
         error_dict={
            '1':UnAuthorizedException,
            '2':BusinessRuleException,
            '3':ForbiddenException
            }
         if code in error_dict:
            return error_dict[code]
   return InternalServerException



class TestErrorGenerator(object):
    def __init__(self, error):
        self.exception = error

    def generateError(self):
        return self.exception
