"""this module returns information from the
config.json file"""

import json
import logging

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def get_key(k_type) -> str:
    """this function returns the API key for the selected API given by k_type"""
    logging.info("Keys extracted by get_key()")
    with open('config.json', 'r') as file:
        json_file = json.load(file)
    keys = json_file["API-keys"]
    if k_type == "weather":
        return keys['weather_api']
    else:
        return keys['news_api']

def get_location(l_type) -> str:
    """this function returns the required location given by l_type """
    logging.info("Location extracted by get_location()")
    with open('config.json', 'r') as file:
        json_file = json.load(file)
    locations = json_file["location"]
    if l_type == "city":
        return locations['city']
    elif l_type == "nation":
        return locations['nation']
    else:
        return locations['country']

def get_urls(u_type) -> str:
    """this function returns the required base URL given by u_type """
    logging.info("URLs extracted by get_urls()")
    with open('config.json', 'r') as file:
        json_file = json.load(file)
    urls = json_file["base-URLs"]
    if u_type == "weather":
        return urls['weather_url']
    else:
        return urls['news_url']

def get_image() -> str:
    """this function returns the homepage image"""
    with open('config.json', 'r') as file:
        json_file = json.load(file)
    image = json_file["image"]
    return image

if __name__ == '__main__':
    logging.info("Extract JSON Module Tested")
    print(get_key("weather"))#tests the function
    print(get_location("city"))#tests the function
    print(get_urls("weather"))#tests the function
    print(get_image())#tests the function
