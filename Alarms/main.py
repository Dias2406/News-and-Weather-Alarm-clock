"""Alarms and notifications scheduler"""

from flask import Flask, request, render_template, redirect
import time, sched, pyttsx3, logging
import weather_news
from datetime import datetime


s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
engine = pyttsx3.init()
alarms = []
notifications = []
notifications_list = []
seen = set()

@app.route('/')
@app.route('/index')
def hello():
    """Returns the web-page with alarms set by user and notifications about news,COVID data,Weather"""
    s.run(blocking=False)

    if request.args.get("alarm"):
        #sets an alarm
        alarm_time = request.args.get("alarm")
        content_label = request.args.get("two")
        alarms.append({"title": "Alarm is set on: " + str(alarm_time[0:10]) + " " + "at: " + str(alarm_time[-5:]), "content": content_label})
        logging.info("Alarm is set on: " + str(alarm_time[0:10]) + " " + "at: " + str(alarm_time[-5:]) + "Content: " + str(content_label))

        for i in range(len(alarms)):
            if alarms[i]['content'] == content_label:
                #converts alarm time and date to delay and shedules an event
                now = datetime.now()
                user_date = datetime(int(alarm_time[0:4]), int(alarm_time[5:7]), int(alarm_time[8:10]), int(alarm_time[-5:-3]), int(alarm_time[-2:]))
                delay = datetime.timestamp(user_date) - datetime.timestamp(now)
                event1 = s.enter(int(delay), 1, announce, [alarms[i]['content'],])
                #deletes alarm after announcement
                event2 = s.enter(int(delay), 2, delete_alarm, [alarms[i]['content'],])
                if request.args.get("weather"):
                    event3 = s.enter(int(delay), 3, announce, [notifications-list[0]['content'],])
                if request.args.get("news"):
                    event4 = s.enter(int(delay), 4, announce, [notifications_list[1]['content'],])
                break

    alarm_item = request.args.get("alarm_item")
    if alarm_item:
        #cancels alarm
        cancel_alarm(alarm_item)
        logging.info("Alarm is canceled by user")

    #saves weather in notifications
    content_weather = weather_news.weather("config.json")
    notifications.append({"title": "Weather", "content": content_weather})

    #saves COVID information in notifications
    content_covid = weather_news.covid("config.json")
    notifications.append({"title": "Covid Data", "content": content_covid})

    for article in weather_news.news("config.json"):
        #saves news in notifications
        content_news = article["title"]
        notifications.append({"title": "News", "content": "Title of the news: " + str(content_news) + ", " + "\n Url: " + str(article["url"])})

    notif = request.args.get("notif")
    if notif:
        #deletes notifications
        delete_notification(notif)
        logging.info("Notification is deleted")

    for item in notifications:
        #deletes duplicates in the notifications
        t = tuple(item.items())
        if t not in seen:
            seen.add(t)
            notifications_list.append(item)

    return render_template('index.html', title = "Alarms and notification", alarms = alarms, notifications=notifications_list, image='alarms.png')


def announce( announcement: str):
    """Returns text-to-speach announcements"""
    try:
        engine.endLoop()
    except:
        logging.error("Error in pyttsx3.engine.endloop. Error ignored, programm allowed to continue")
    engine.say(announcement)
    engine.runAndWait()


def delete_notification( notification: str ):
    """Returns a list of notifications with deleted notification"""
    for i in range(len(notifications_list)):
        if notifications_list[i]['title'] == notification:
            del notifications_list[i]
            break
    return notifications

def cancel_alarm( alarm: str ):
    """Returns a list of alarms with deleted alarm"""
    for i in range(len(alarms)):
        if alarms[i]['title'] == alarm:
            del alarms[i]
            break
    return alarms

def delete_alarm( alarm: str ):
    """Returns a list of alarms with deleted alarm"""
    for i in range(len(alarms)):
        if alarms[i]['content'] == alarm:
            del alarms[i]
            break
    return alarms



if __name__ == '__main__':
    logging.basicConfig(filename = 'sys.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(name)s : %(message)s')
    app.run()
