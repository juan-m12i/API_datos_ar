# coding: utf-8
#import os
#import sys
import json
#import base64
#from collections import namedtuple

if (sys.version_info > (3, 0)):
    # Python 3
    from urllib.request import urlopen, Request
    from urllib.parse import urljoin, urlencode
else:
    # Python 2
    from urlparse import urljoin
    from urllib import urlencode
    from urllib2 import Request, urlopen, HTTPError

url = "http://apis.datos.gob.ar/series/api/series?"


COLLAPSE_VALUES = ["year", "quarter", "month", "week", "day"]
COLLAPSE_AGGREGATION_VALUES = ["avg", "sum", "end_of_period", "min", "max"]



def get_datos(series, format = "json", start_date = None, end_date = None, collapse = None, collapse_aggregation = None


