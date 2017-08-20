def dayDecoder(data):

    # 最高温度と最低温度のどちらかがない場合
    if data["temperature"]["min"] == None or data["temperature"]["max"] == None:
        return {\
            "date":data["date"],\
            "telop":data["telop"],\
            "telop":data["telop"],\
            "temperature":None,\
            "umbrella":"雨" in data["telop"]
            }

    # 最高温度と最低温度の両方ある場合
    else:
        # 温度は°Cのみ使用（celsius） °Fは"fahrenheit"を指定
        return {\
            "date":data["date"],\
            "telop":data["telop"],\
            "telop":data["telop"],\
            "temperature":{\
                "min":data["temperature"]["min"]["celsius"],\
                "max":data["temperature"]["max"]["celsius"],\
                },\
            "umbrella":"雨" in data["telop"]
            }



def decoder(infData):

    # 明後日がデータない時があるので、その対応
    todayWeather = None
    tomorrowWeather = None
    dayAfterTomorrowWeather = None

    for inf in infData["forecasts"]:

        if inf["dateLabel"] == "今日":
            todayWeather = dayDecoder(inf)

        elif inf["dateLabel"] == "明日":
            tomorrowWeather = dayDecoder(inf)

        elif inf["dateLabel"] == "明後日":
            dayAfterTomorrowWeather = dayDecoder(inf)


    # 返すデータを作る
    retData = {\
        "place":infData["location"],\
        "presentationTime":infData["publicTime"],\
        "today":todayWeather,\
        "tomorrow":tomorrowWeather,\
        "dayAfterTomorrow":dayAfterTomorrowWeather
        }

    return retData
