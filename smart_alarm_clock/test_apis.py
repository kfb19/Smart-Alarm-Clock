"""this module is designed to test the version of the APIs required
to see if they are up to date so the program can be run"""

import logging
from news_api import check_news_version
from weather_api import check_weather_version
from covid_api import check_covid_version

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def test_api() -> bool:
    """this function checks to see if each API can be properly set up
    and if there is an error, it is logged and the user
    is told to abort the program"""
    weather = False
    news = False
    covid = False
    if check_weather_version():
        logging.info("Weather API version is up to date (check_weather_version())")
        weather = True
    else:
        logging.info("Weather API version is not up to date (check_weather_version()) - ACTION REQUIRED")
    if check_news_version():
        logging.info("News API version is up to date (check_news_version())")
        news = True
    else:
        logging.info("News API version is not up to date (check_news_version()) - ACTION REQUIRED")
    if check_covid_version():
        logging.info("Covid-19 API version is up to date (check_covid_version())")
        covid = True
    else:
        logging.info("Covid-19 API version is not up to date (check_covid_version()) - ACTION REQUIRED")
    return bool(weather and news and covid)

if __name__ == '__main__':
    logging.info("Test API Module Tested")
    print(test_api())#tests the function
