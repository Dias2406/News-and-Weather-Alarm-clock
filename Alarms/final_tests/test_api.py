import requests
import json

def test_apicall_weather():
    with open("config.json", 'r') as f:
        json_file = json.load(f)
    api_key = json_file["API-keys"]
    weather_api = api_key["weather"]
    weather_description = json_file["Weather_description"]
    city_name = weather_description["City_name"]
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + weather_api + "&q=" + city_name
    response = requests.get(complete_url)
    assert response.status_code == 200

def test_apicall_news():
    with open("config.json", 'r') as f:
        json_file = json.load(f)
    api_key = json_file["API-keys"]
    news_api = api_key["news"]
    news_description = json_file["News_description"]
    country = news_description["Country"]
    base_url = "https://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country + "&apiKey=" + news_api
    # print response object
    response = requests.get(complete_url)
    assert response.status_code == 200
