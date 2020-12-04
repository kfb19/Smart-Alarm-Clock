"""this module collects current news headlines from the API"""

import logging
import requests
from extract_json import get_key
from extract_json import get_location
from extract_json import get_urls

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
BASE_URL = get_urls("news")
API_KEY = get_key("news")
COUNTRY = get_location("country")
COMPLETE_URL = BASE_URL + "country=" + COUNTRY + "&apiKey=" + API_KEY
response = requests.get(COMPLETE_URL)

def get_news() -> list:
    """this function gets the current news information using an API"""
    logging.info("Articles returned by get_news()")
    news_dict = response.json()
    articles = news_dict["articles"]
    news_articles = []
    for article in articles:
        news_articles.append({'name':article['title'], 'url':article['url']})
    return news_articles

def check_news_version() -> bool:
    """this function checks for the correct setup of the API"""
    try:
        news_dict = response.json()
        return True
    except:
        return False

if __name__ == '__main__':
    logging.info("News API Module Tested")
    print(get_news())#tests the function
    print(check_news_version())#tests the function
