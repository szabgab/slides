import configparser
import requests
import sys

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def main():
    if len(sys.argv) != 2:
        exit("Usage: {} LOCATION".format(sys.argv[0]))
    location = sys.argv[1]

    api_key = get_api_key()
    weather = get_weather(api_key, location)

    #print(weather)
    print(weather['main']['temp'])


if __name__ == '__main__':
    main()
