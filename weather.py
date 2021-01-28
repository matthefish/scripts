import requests
import sys
import pprint
import json

key = 'a30a79db14d829de8ef5b013c14c87ae'
cityname = sys.argv[1]
url = f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={key}&units=metric'
page = requests.get(url)
content = json.loads(page.content.decode('utf-8'))

def currentWeather():
    global content
    try:
        keys = [i for i in content['main']]
        values = [i for i in content['main'].values()]
        return dict(zip(keys,values))
    except:
        return False

if __name__ == '__main__':
    weather = currentWeather()
    if weather != False:
        for i in weather.keys():
            print(i, ':',weather[i])
    else:
        print('could not find weather for:', cityname)
