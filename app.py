import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from datetime import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)
def format_timestamp(timestamp):
    try:
        return datetime.fromisoformat(timestamp).strftime('%B %d, %Y %I:%M %p')
    except (ValueError, TypeError):
        return "N/A"

@app.route('/')
def get_current_info():
    
    # API request URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.8041&longitude=-93.1669&daily=sunset,sunrise&models=gfs_seamless&current=is_day,precipitation,temperature_2m&timezone=America%2FChicago&forecast_days=1&wind_speed_unit=mph&precipitation_unit=inch&temperature_unit=fahrenheit"
    
    response = requests.get(url, verify=False)  # Open link, verify=False to ignore SSL warnings
    data = response.json()  # Convert to JSON

    # Extract relevant data from the API response
    last_updated = data["current"].get("time", None)
    current_precipitation = data["current"].get("precipitation", None)
    current_temp = data["current"].get("temperature_2m", None)
    sunset_time = data["daily"].get("sunset", [None])[0]
    sunrise_time = data["daily"].get("sunrise", [None])[0]

    # Format the timestamps for readability
    last_updated = format_timestamp(last_updated)
    sunset_time = format_timestamp(sunset_time)
    sunrise_time = format_timestamp(sunrise_time)

    # Get current time and date
    timezone = pytz.timezone('America/Chicago')  # Set timezone to Chicago
    current_time = datetime.now(timezone).strftime("%I:%M:%S %p")
    current_date = datetime.now(timezone).strftime("%Y-%m-%d")  # Date format

    # Return data to the HTML template
    return render_template("index.html", 
                           lastUpdated=last_updated, 
                           currentPrecipitation=current_precipitation, 
                           currentTemp=current_temp,
                           currentTime=current_time,
                           currentDate=current_date,
                           sunsetTime=sunset_time,
                           sunriseTime=sunrise_time)

if __name__ == '__main__':
    app.run(debug=True)



# if __name__ == '__main__':
#     user_input = input("Do you want to start the Flask app? (yes/no): ").strip().lower()
    
#     if user_input == "yes":
#         print("Starting Flask app...")
#         app.run(debug=True)
#     else:
#         print("Flask app will not start.")
