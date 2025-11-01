#  file about the weather_fetcher.py
import requests

class WeatherFetcher:
    def __init__(self, api_key):  
        # the step indicates the initializing the weather fetcher with the help  of api and base url for the openweathermap
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, city_name):
        #parameters for the api request provided
        params = {
            "q": city_name,#city name parameter 
            "appid": self.api_key,#authentication of api key
            "units": "metric"#requests to provide temperature in celsius
        }
        try:
            #making a get request to openweathermap api
            response = requests.get(self.base_url, params=params)
            # raising expection for http errors
            response.raise_for_status()
            #parse json response from api
            data = response.json()
            #structure relevant weather data
            weather = {
                "city": city_name,#city name
                "temp": data["main"]["temp"],#current temperature,
                "humidity": data["main"]["humidity"], #percentage of humidity
                "condition": data["weather"][0]["main"]#weather condition
            }
            return weather
        except requests.exceptions.HTTPError:
            #handling http errors
            print("Invalid city name or API error.")
            return None
        except Exception as e:
            # handling un expected errors
            print("Error:", e)
            return None