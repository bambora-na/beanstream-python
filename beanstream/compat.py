from __future__ import unicode_literals

try:  # Python 3
    from http.client import HTTPSConnection
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.parse import parse_qs

    def open_url(request, data):
        return urlopen(request, bytes(data, 'utf-8'))

    def get_status(response):
        return response.status
except ImportError:  # Python 2
    from httplib import HTTPSConnection
    from urllib import urlencode, addinfourl
    from urllib2 import urlopen
    from urllib2 import Request
    from urlparse import parse_qs

    def open_url(request, data):
        return urlopen(request, data.encode('utf-8'))

    def get_status(response):
        if isinstance(response, addinfourl):
            return response.code
        return response.status

try:
    from enum import Enum
except ImportError:
    raise ImportError('Enum class not found; please install enum34')