"""this module collects Covid-19 information from the API"""

import logging
from uk_covid19 import Cov19API
from extract_json import get_location

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def set_up_api():
    """this function sets up the api for use"""
    filter_specs = ['areaType=nation', 'areaName=' + get_location('nation')]
    cases_and_deaths = {
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
    }
    api = Cov19API(filters=filter_specs, structure=cases_and_deaths)
    return api

def get_covid() -> str:
    """this function gets the current coronavirus information using an API"""
    logging.info("Covid information returned by get_covid()")
    api = set_up_api()
    data = api.get_json()
    total_deaths = data['data'][0]['cumDeathsByDeathDate']
    total_cases = data['data'][0]['cumCasesByPublishDate']
    new_deaths = data['data'][0]['newDeathsByDeathDate']
    new_cases = data['data'][0]['newCasesByPublishDate']
    if new_deaths is None or total_deaths is None:
        new_deaths = data['data'][1]['newDeathsByDeathDate']
        total_deaths = data['data'][1]['cumDeathsByDeathDate']
    t_deaths = "The number of total deaths is " + str(total_deaths)
    t_cases = " and the number of total cases is " + str(total_cases) + "."
    n_deaths = " The number of new deaths is " + str(new_deaths)
    n_cases = " and the number of new cases is " + str(new_cases) + "."
    covid_info = t_deaths + t_cases + n_deaths + n_cases
    return covid_info

def check_covid_version() -> bool:
    """this function checks to see if the API version is correct"""
    try:
        api = set_up_api()
        return True
    except:
        return False

if __name__ == '__main__':
    logging.info("Covid API Module Tested")
    print(get_covid())#tests the function
    print(check_covid_version())#tests the function
