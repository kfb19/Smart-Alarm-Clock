"""this module collects current weather information from the API"""

import logging
import requests
from extract_json import get_key
from extract_json import get_location
from extract_json import get_urls

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
BASE_URL = get_urls("weather")
API_KEY = get_key("weather")
CITY_NAME = get_location("city")
COMPLETE_URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY_NAME
response = requests.get(COMPLETE_URL)

def get_weather() -> str:
    """this function gets the current weather information using an API"""
    logging.info("Weather returned by get_weather()")
    weather_dict = response.json()
    description = "The current weather is " + weather_dict["weather"][0]["description"]
    temp_celcuis = round(((weather_dict["main"]["temp"]) - 273), 2)
    temperature = " and the temperature is " + str(temp_celcuis) + "°C."
    weather = description + temperature
    return weather

def check_weather_version() -> bool:
    """this module checks to see if the API setup is correct"""
    try:
        weather_dict = response.json()
        return True
    except:
        return False

if __name__ == '__main__':
    logging.info("Weather API Module Tested")
    print(get_weather())#tests the function
    print(check_weather_version())#tests the function
