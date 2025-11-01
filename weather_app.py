# file consists of weather_app.py where actual code is present to run the application
from weather_fetcher import WeatherFetcher
from weather_logger import WeatherLogger

class WeatherApp:
    def __init__(self, api_key):
        #initialsing the main app application with its components
        self.fetcher = WeatherFetcher(api_key)# handles compunication api
        self.logger = WeatherLogger()#data persistance handling

    def run(self):
        #main loop
        while True:
            #getting user input for city name
            city = input("Enter city name (or 'exit' to quit): ").strip()
            #checking whether user is wiiling to exists the application
            if city.lower() == "exit":
                print("Exiting application.")
                break
            #fetching the weather data for the specified city
            weather = self.fetcher.fetch(city)
            #if the weather data was successfully retreived or not?
            if weather:
                #displaying the weather information to user
                print(f"{weather['city']}: {weather['temp']}°C, Humidity: {weather['humidity']}%, Conditions: {weather['condition']}")
                #weather data loggging to data base
                self.logger.log(weather)

if __name__ == "__main__":
    # my own api key for openweathermapservice
    API_KEY = "5ffc534ea4451b258d5f7ee41d5a2c8f"
    #create and run the weather application 
    app = WeatherApp(API_KEY)
    app.run()