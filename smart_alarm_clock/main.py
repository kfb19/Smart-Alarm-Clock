"""Copyright (c) Kate Belson. All Rights Reserved.
The source code contained in this file and all intellectual property embodied in
or covering the source code is the property of Kate Belson.
This heading must NOT be removed from this file. t
This module is used to run the smart alarm
clock system, providing news, weather and Covid-19
updates as well as user-set alarms"""

import logging
import time
import datetime
import sched
import pyttsx3
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from test_apis import test_api
from news_api import get_news
from weather_api import get_weather
from covid_api import get_covid
from extract_json import get_image
from get_notifications import create_notifications

def refresh_alarm() -> str:
    """this function refreshes the page every hour and updates the notifications"""
    logging.info("Page refreshed by refresh_alarm()")
    notifications = create_notifications()
    s.enter(3600,1,refresh_alarm)
    return "Alarm refreshed"

logging.basicConfig(filename='pysys.log',level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.info("*** Program Started ***")
if test_api():
    logging.info("API versions are up to date.")
    app = Flask(__name__)
    s = sched.scheduler(time.time, time.sleep)
    alarms = []
    notifications = create_notifications()
    refresh_alarm()
else:
    logging.info("API version issue detected by test_api(). Please update API versions.")
    print("Please close the program. API version issue detected by test_api(). Please update API versions.")

def set_off_alarm(announcement:str):
    """this function announces the scheduled alarm announcement using text-to-speech"""
    engine = pyttsx3.init()
    try:
        engine.endLoop()
    except:
        pass
    engine.say(announcement)
    engine.runAndWait()
    engine.stop()
    logging.info("Alarm announced in set_off_alarm(): " + announcement)
    return redirect('/index')

def set_alarms(alarm:dict, s):
    """this function enters the alarms to the scheduler"""
    time = alarm['title'][:10:] + " " + alarm['title'][11::]
    alarm_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")
    delay = (alarm_time - datetime.datetime.strptime(str(datetime.datetime.now()).rpartition(':')[0], "%Y-%m-%d %H:%M")).total_seconds()
    if alarm['news'] and alarm['weather']:
        message = alarm['content'] + " - Top news stories - One - " + (get_news()[-1])['name'] + " - two - " + (get_news()[-2])['name'] + " - three - " + (get_news()[-3])['name'] + " - " + get_weather() + " - Covid-19 update - " + get_covid()
    elif alarm['news']:
        message = alarm['content'] + " - Top news stories - One - " + (get_news()[-1])['name'] + " - two - " + (get_news()[-2])['name'] + " - three - " + (get_news()[-3])['name'] + " - Covid-19 update - " + get_covid()
    elif alarm['weather']:
        message = alarm['content'] + " - " + get_weather() + " - Covid-19 update - " + get_covid()
    else:
        message = alarm['content'] + " - Covid-19 update - " + get_covid()
    s.enter(int(delay),1,set_off_alarm,(message,))
    logging.info("Alarm set in set_alarms(): " + message)

def set_new_alarm():
    """this function creates the alarm"""
    time = request.args.get('alarm')
    name = request.args.get('two')
    news = request.args.get('news')
    weather = request.args.get('weather')
    date = time[:10:] + " " + time[11::]
    if news is None:
        news = False
    else:
        news = True
    if weather is None:
        weather = False
    else:
        weather = True
    alarms.insert(0, {"title":date, "content":name, "news":news, "weather":weather, "id":1})
    set_alarms(alarms[0], s)
    logging.info("Alarm created in set_new_alarm()")

def delete_alarm():
    """this function deletes alarms"""
    name = request.args.get('alarm_item')
    logging.info("Alarm deleted in delete_alarm(): " + name)
    for alarm in alarms:
        if alarm['title'] == name:
            alarms.remove(alarm)

def delete_notification():
    """this function deletes notifications"""
    name = request.args.get('notif')
    logging.info("Notification deleted in delete_notification(): " + name)
    for notif in notifications:
        if notif['title'] == name:
            notifications.remove(notif)     

@app.route('/index')
def smart_alarm_homepage():
    """this function displays the main homepage, containing notifications and alarms"""
    s.run(blocking=False)
    try:
        delete_alarm()
    except:
        pass
    try:
        delete_notification()
    except:
        pass
    try:
        set_new_alarm()
        return redirect(request.path, code=302)    
    except:
        pass
    return render_template('index.html', title='Alarm Clock', notifications=notifications, image=get_image(), alarms=alarms)

if __name__ == '__main__':
    app.run()
