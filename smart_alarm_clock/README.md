
# Smart Alarm Clock

## Introduction

Smart Alarm Clock is a python program that lets the user set alarms and see recent news, Covid-19 and weather updates. The alarms have options to add on news or weather briefings and all alarms come with a COVID-19 briefing focused on cases and deaths. The user can delete alarms and notifications as they wish and the alarms are announced using a text-to-speech module. 

## Prerequisites

Developed in Python 3.8.6 

Before running the program, the user must add their API keys into the file config.json, found in the smart_alarm_clock folder. API keys are needed for the weather API ([get key here](https://openweathermap.org/api)) and the news API ([get key here](https://newsapi.org/)).

The user also needs to set their location in the file config.json: 'city' to their city, 'nation' to their country within Great Britain, and 'country' to 'gb' as this program is designed to solely operate in Great Britain. 

The user may also use the file config.json to change the URL of the APIs if the program is run and discovers that the API version has changed, which will be logged in the log file pysys.log - if this is the case, then a new URL for the version will need to be entered into config.json. 

The user has the option to change the image displayed on the Smart Alarm Clock webpage - to do this, they must save the image in the folder \smart_alarm_clock\static\images and then change the name of the image in the file config.json. 

## Installation

Prior to running the program, use the packet manager pip to install the module pyttsx3 for text-to-speech.

```bash
pip install pyttsx3
```
The user will also need to install the Covid-19 API using pip.

```bash
pip install uk-covid19 
```
In order to test the program, the user will need to install pytest using pip. 
```bash
pip install pytest
```
## Getting Started 

Use command line to call python (from the directory smart_alarm_clock) to run the program, then open a web browser (Edge recommended as used for development) and enter the URL: http://127.0.0.1:5000/index and the page will load. Notifications (news, weather and Covid-19) will be shown on the right, alarms on the left. Alarms can be set using the form in the middle of the screen. As long as the program remains running, alarms can be set in advance for any time. Click on the cross by a notification or alarm to delete it. Crtl-C in the command line will stop the program. 

```bash
cd smart_alarm_clock
python main.py
```

## Developer Documentation
Modules: 
1. main.py - this module is used to run the smart alarm clock system, providing news, weather and Covid-19
updates as well as user-set alarms. 
	Functions: 
	- refresh_alarm() - this function refreshes the page every hour and updates the notifications
	- set_off_alarm(announcement) -this function announces the scheduled alarm announcement using text-to-speech
	- set_alarms(alarm, s) - this function enters the alarms to the scheduler
	- set_new_alarm() - this function creates the alarm
	- delete_alarm() - this function deletes alarms
	- delete_notification() - this function deletes notifications
	- smart_alarm_homepage() - this function displays the main homepage, containing notifications and alarms
2. covid_api.py - this module collects Covid-19 information from the API. 
      Functions:
	- set_up_api() - this function sets up the API for use 
	- get_covid() - this function gets the current coronavirus information using an API 
	- check_covid_version() - this function checks to see if the API version is correct 
3. news_api.py - this module collects current news headlines from the API
	Functions:
	- get_news() - this function gets the current news information using an API 
	- check_news_version() - this function checks for the correct setup of the API
4.  weather_api.py - this module collects current weather information from the API
	Functions:
	- get_weather() - this function gets the current weather information using an API
	- check_weather_version() - this module checks to see if the API setup is correct 
5. test_apis.py - this module is designed to test the version of the APIs required
to see if they are up to date so the program can be run
	Functions:
	- def test_api() - this function checks to see if each API can be properly set up and if there is an error, it is logged and the user is told to abort the program
6. get_notifications.py - this module returns the required notifications
	Functions:
	- create_notifications() - this function creates and returns the notifications 
7. extract_json.py - this module returns information from the config.json file
	Functions:
	- get_key(k_type) - this function returns the API key for the selected API given by k_type 
	- get_location(l_type) - this function returns the required location given by l_type 
	- get_urls(u_type) - this function returns the required base URL given by u_type 
	- get_image() - this function returns the homepage image 


## Testing 

To run module tests: 
- In command line, use the python command to run each module independently of main.py in order to see a demonstration of information returned by the functions. 
- Check command line to see the information returned and check the log file pysys.log in order to see the functions called when the tests are run. It is also logged that this exercise is a test. 
- Below are the commands that need to be run. 
```bash
python covid_api.py
python news_api.py
python weather_api.py
python test_apis.py
python get_notifications.py
python extract_json.py
```
To run unit tests:
- Unit tests are run using pytest. 
- In command line, make sure you are in the smart_alarm_clock directory. 
- Run the command python -m pytest in order to run the tests. 
```bash
cd smart_alarm_clock
python -m pytest
```
The application automatically tests external services and if there is a version issue or similar with the APIs, a log is created and the user is warned to terminate the program as it will not run. 
## Authors 

- Kate Frances Belson (Undergraduate Student studying BSc Computer Science at the University of Exeter)

## Handle

https://github.com/kfb19/Smart-Alarm-Clock
## Publish Date 

- Version 0.0.1 was published on 04/12/2020

## License
[MIT](https://choosealicense.com/licenses/mit/)