# The WeatherLogger class is responsible for persisting weather data to storage, managing historical records, and providing data retrieval capabilities. It handles the storage of weather information fetched by the WeatherFetcher for future reference and analysis.
#  this file  consists of weather_logger.py
import sqlite3
from datetime import datetime

class WeatherLogger:
    def __init__(self, db_path="weather_log.db"):
        # intialising the data base connection with sqllite db
        self.conn = sqlite3.connect(db_path)
        #the line ensures the required table exists
        self.create_table()

    def create_table(self):
        #creating the logs table if not present
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY,
                    city TEXT,
                    temp REAL,
                    humidity INTEGER,
                    condition TEXT,
                    timestamp TEXT
                )
            """)

    def log(self, weather_data):
        # inserting the new weather data into the datbase
        with self.conn:
            self.conn.execute("""
                INSERT INTO logs (city, temp, humidity, condition, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (
                weather_data["city"],
                weather_data["temp"],
                weather_data["humidity"],
                weather_data["condition"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ))
