import json
import requests
from uk_covid19 import Cov19API
import main

def weather( filename: str ):
    """Returns the weather desriptions in the region"""
    with open(filename, 'r') as f:
        json_file = json.load(f)
    api_key = json_file["API-keys"]
    weather_api = api_key["weather"]
    weather_description = json_file["Weather_description"]
    city_name = weather_description["City_name"]

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + weather_api + "&q=" + city_name
    # print response object
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        air_temperature = int(y["temp"] - 273)
        feels_like_temperature = int(y["feels_like"] - 273)
        z = x["weather"]
        weather_description = z[0]["description"]
        return(" Temperature = " + str(air_temperature) + " celcius" + ", " +
            "\n Feels like Temperature = " + str(feels_like_temperature) + " celcius" + ", " +
            "\n description = " + str(weather_description)) + "."
def news( filename: str ):
    """Returns most recent news"""
    with open(filename, 'r') as f:
        json_file = json.load(f)
    api_key = json_file["API-keys"]
    news_api = api_key["news"]
    news_description = json_file["News_description"]
    country = news_description["Country"]

    base_url = "https://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country + "&apiKey=" + news_api
    # print response object
    response = requests.get(complete_url)
    news_dict = response.json()
    articles = news_dict["articles"]
    return articles


def covid( filename: str ):
    """Returns COVID data in the England"""
    with open(filename, 'r') as f:
        json_file = json.load(f)
    england_only = ['areaType=nation','areaName=England']
    cases = json_file["Covid_cases_and_deaths"]
    api = Cov19API(filters=england_only,structure=cases,latest_by="newCasesByPublishDate")
    data = api.get_json()
    info = data["data"]
    date = info[0]["date"]
    area = info[0]["areaName"]
    new_cases = info[0]["newCasesByPublishDate"]
    cum_cases = info[0]["cumCasesByPublishDate"]
    new_death = info[0]["newDeathsByDeathDate"]
    if int(new_cases)>20000:
        #announces a warning if a threshold of daily infection is reached
        main.announce("The daily number of cases in England increased, be aware, wash your hands and keep distance")
    return(" Date of publishing:" + str(date) + ", " +
        "\n Country:" + str(area) + ", " +
        "\n New cases:" + str(new_cases) + ", " +
        "\n Total cases:" + str(cum_cases) + ", " +
        "\n New deathes:" + str(new_death)) + "."
