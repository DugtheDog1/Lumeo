
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from datetime import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_current_info():
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.8&longitude=-93.17&current=temperature_2m,is_day,weather_code&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch"
    
    response = requests.get(url, verify=False)  # Open link, verify=False to ignore SSL warnings
    data = response.json()  # Convert to JSON

    # Extract relevant data
    current_is_day = data["current"].get("is_day", None)
    current_time_utc = data["current"].get("time", None)
    current_precipitation_status = data["current"].get("precipitation", None)
    current_overall_status = data["current"].get("weather_code", None)

    # Convert the UTC time to local time (Central Time)
    if current_time_utc:
        # Convert the string to a datetime object
        utc_time = datetime.fromisoformat(current_time_utc)
        # Get the UTC timezone and local timezone (replace with your actual local timezone, e.g., 'America/Chicago' for Minnesota)
        utc_zone = pytz.UTC
        local_zone = pytz.timezone('America/Chicago')
        # Make the datetime object timezone-aware (in UTC)
        utc_time = utc_zone.localize(utc_time)
        # Convert to local time
        local_time = utc_time.astimezone(local_zone)
        # Format the local time
        current_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        current_time = None


    # Return data to the HTML template
    return render_template("index.html", 
                           isDay=current_is_day, 
                           currentTime=current_time, 
                           currentPrecipitationStatus=current_precipitation_status, 
                           currentOverallStatus=current_overall_status)



if __name__ == '__main__':
    app.run(debug=True)


# if __name__ == '__main__':
#     user_input = input("Do you want to start the Flask app? (yes/no): ").strip().lower()
    
#     if user_input == "yes":
#         print("Starting Flask app...")
#         app.run(debug=True)
#     else:
#         print("Flask app will not start.")


