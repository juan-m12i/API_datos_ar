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
REPRESENTATION_VALUES = ["value", "change", "percent_change", "percent_change_a_year_ago"]
FORMAT_VALUES = ["json", "csv"]
HEADER_VALUES = ["titles", "ids", "descriptions"]
SORT_VALUES = ["asc", "desc"]
METADATA_VALUES = ["none", "simple", "full", "only"]


def get_datos(ids, format = "json", start_date = None, end_date = None, collapse = None,
              collapse_aggregation = None, representation = "value", limit = 100, start = 0,
              header = "titles", sort = "asc", 
              
              



"""              
              
              Nombre	Requerido	Tipo	Default	Ejemplos

collapse	No	Uno de: day, week, month, quarter, year	La frecuencia propia de la serie	collapse=year
collapse=quarter
collapse_aggregation	No	Uno de: avg, sum, end_of_period, min, max	avg	collapse_aggregation=sum
limit	No	Número entero positivo, no mayor que 1000.	100	limit=50
start	No	Número entero positivo o 0.	0	start=100
start_date	No	Fecha y hora en formato ISO 8601.

Si no se especifica este parámetro, se devuelven los datos disponibles para la serie o series desde el valor más antiguo.	N/A	start_date=2016-11-30
start_date=2016-11
start_date=2016
end_date	No	Fecha y hora en formato ISO 8601.

Si no se especifica este parámetro, se devuelven los datos disponibles para la serie o series hasta el valor más reciente.	N/A	end_date=2016-11-30
end_date=2016-11
end_date=2016
format	No	Uno de: json, csv	json	format=csv
header	No	Uno de: titles, ids, descriptions	titles	header=ids
sort	No	Uno de: asc, desc	asc	sort=desc
metadata	No	Uno de: none, simple, full, only	simple	metadata=none

"""
