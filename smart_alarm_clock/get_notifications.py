"""this module returns the required notifications"""

import logging
from flask import Markup
from news_api import get_news
from weather_api import get_weather
from covid_api import get_covid

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def create_notifications() -> list:
    """this function creates and returns the notifications"""
    logging.info("Notifications returned by create_notifications()")
    notifications = []
    news = get_news()
    counter = len(news)
    for article in news:
        notifications.insert(0, {"title":"News Update " + str(counter), "content":Markup("<a href=" + article['url'] + ">" + article['name'] + "<\a>")})
        counter = counter - 1
    weather = get_weather()
    notifications.insert(0, {"title":"Weather Update", "content":weather})
    covid = get_covid()
    notifications.insert(0, {"title":"Covid-19 Update", "content":covid})
    return notifications

if __name__ == '__main__':
    logging.info("Notification Module Tested")
    print(create_notifications())#tests the function
