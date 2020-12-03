# CA3: News and Weather Alarm clock
## Introduction
This project includes an alarm clock and notifications (such as news, weather and COVID-19 information updates). User can set up an alarm in order to keep informed (using text-to-speech announcements) about recent news, weather and COVID-19 statistics in the country.
## Prerequisites
The project work on Python3 programming language. You will need to install python3 interpreter and create new virtual environment. To install Python3 follow the link below:
https://www.python.org/downloads/ 

Also, in order to get an up-to-date weather report you will need sign up for an API key - please only use the free version (links bellow):

https://openweathermap.org

https://newsapi.org/
## Installations
In order to start using the project, you will need to install flask, pyttsx3, requests, schedule, pytest modules. Navigate to the Alarms folder using `cd` and install requirements:

`pip3 install -r requirements.txt`
## Project using
Before activating the app, you need to open config.json file and insert your API keys for weather and news. Then, open the terminal and navigate to the directory where you saved the project (using cd) and check that it’s there (using ls). Then run the app using:

`$ python3 main.py`

Open a browser and navigate to http://127.0.0.1:5000/

Now, in the notification title, you can see the weather in the Exeter (the city can be changed in the config.json file), recent Covid-19 updates and recent News in UK (country can be changed in the config.json file). You can set up a text-to-speech announcement alarm by choosing date, time and include news (Covid-19 updates) or weather briefings. Furthermore, if the threshold of the Covid-19 daily new cases (20000 new cases per day) will be reached, you will be notified instantly by text-to-speech announcement.

## Testing
To test the API calls, first of all you need to ensure that you installed pytest. After, in the terminal, navigate to Alarms directory using cd and write the code:

`$ python3 -m pytest`

If no error occurs, it means API calls are working correctly
## Developer Documentations
In this sections, you will see how to change information you need and observe the what events the system is responding to and how that is affecting the behaviour of the system.
### Config file
You can find config.json file in the Alarms directory which includes your API calls, filepaths of image and logfile, city name for weather, country name for news and information which included in Covid-19 Updates. This resources you can use to customise the app as you want. For example, if you want to know the weather in London, you can change the city_name to London in the config file.
### Log file
In the log file you can see time and date of the requests from flask, error logs entry when an exception is caught and info logs that contains the alarm time and details each time an alarm is entered.
## Author
+ Jakupov Dias - University of Exeter student
## License
This project is licensed under the MIT License - see the LICENSE.txt file for details
