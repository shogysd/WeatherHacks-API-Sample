# coding:utf-8

import urllib.parse
import urllib.request
from IDtran import idTran

def weatherInf(TARGET):

    TARGET_ID = idTran(TARGET)

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
    params = urllib.parse.urlencode({
        'city':TARGET_ID
        }
    )

    response = urllib.request.urlopen(url + params)

    return response.read()
