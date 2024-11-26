WEATHER FETCHER FOR LAGOS STATE

This project fetches weather data for Lagos, Nigeria, using the Tomorrow.io API and stores it in a MongoDB database. The weather data is collected
every minute and saved into he database

WHAT MY PROJECT DOES
Fetches current weather data for Lagos, Nigeria.
Uses the Tomorrow.io API to retrieve the weather data.
Stores the weather data in a MongoDB database (weather_db).
Runs continuously, fetching and storing the data every minute using the APScheduler.

MY STUFFS
Tomorrow.io API Key (Replace PklmgXLhftUOSe3m9tbEMQQFA16dinFL-->this is the one i used for this 
task so you replace it with your own API key)

PYTHON LIBRARIES USED FOR THIS TASK
pymongo
requests
apscheduler

Setup Instruction
1.Ensure you have Python 3 installed. Then, install the required Python libraries:

2.Make sure you have MongoDB installed and running on your machine. If you are using a remote MongoDB instance, update the MongoDB URI in the code accordingly.

3.Get a Tomorrow.io API Key
Sign up at Tomorrow.io and get your API key. Replace the API key in the fetch_weather function:
API_KEY = 'your-api-key-here'

4. Start MongoDB
If you're running MongoDB locally, ensure the MongoDB service is running:

On Windows, open a Command Prompt and run mongod to start the MongoDB server.

5. Run the code
After completing the setup, you can start the script that fetches and stores the weather data:

THIS IS THE COMMAND TO RUN THE CODE
python app.py--->(INPUT YOUR FILE NAME)
The script will now fetch weather data every minute and save it to the MongoDB collection lagos_weather inside the weather_db database.
