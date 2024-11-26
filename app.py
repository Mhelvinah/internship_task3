from pymongo import MongoClient
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["weather_db"]  # Create or access the "weather_db" database
collection = db["lagos_weather"]  # Create or access the "lagos_weather" collection

# Tomorrow.io API endpoint and API key
API_KEY = 'PklmgXLhftUOSe3m9tbEMQQFA16dinFL'  # Replace with your Tomorrow.io API key
LATITUDE = 6.5244  # Latitude for Lagos
LONGITUDE = 3.3792  # Longitude for Lagos
BASE_URL = 'https://api.tomorrow.io/v4/weather/forecast'

def fetch_weather():
    """Fetch weather data for Lagos from Tomorrow.io API."""
    url = f"{BASE_URL}?location={LATITUDE},{LONGITUDE}&apikey={API_KEY}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant weather data
        weather_info = data
        return weather_info
    else:
        print("Error fetching weather data from Tomorrow.io API.")
        return None

def save_weather():
    """Fetch weather and save it to MongoDB."""
    weather_data = fetch_weather()
    if weather_data:
        collection.insert_one(weather_data)  # Insert the weather data into the collection
        print("Weather data has been saved to the database!")

def start_scheduler():
    """Start the scheduler to fetch and save weather data every 1 minute."""
    scheduler = BlockingScheduler()
    scheduler.add_job(save_weather, 'interval', minutes=1)  # Run every 1 minute
    print("Scheduler started. Fetching weather data every 1 minute.")
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
