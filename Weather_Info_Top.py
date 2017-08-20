#coding:utf-8

import json
from CatchWeatherInf import weatherInf
from decoder import decoder

def WeatherInfoTop(TARGET):
    # 気象情報を取得
    # jsonをstrに変換して格納
    infData = json.loads(weatherInf(TARGET))
    decodedData = decoder(infData)
    return decodedData


# デバッグ用
if __name__ == '__main__':
    ret = WeatherInfoTop("Tokyo")
    print(ret)
