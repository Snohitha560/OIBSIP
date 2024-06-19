import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    print("City:", weather_data["name"])
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Humidity:", weather_data["main"]["humidity"], "%")
    print("Weather Conditions:", weather_data["weather"][0]["description"])

def main():
    api_key = "39e5f2002bafacd947c029e8c3258a50"
    city = input("Enter the name of the city: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__== "__main__":
    main()