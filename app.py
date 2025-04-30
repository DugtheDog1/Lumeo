
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_current_info():
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.8041&longitude=-93.1669&hourly=soil_moisture_1_to_3cm,soil_temperature_6cm&current=temperature_2m,is_day,showers,snowfall,rain,precipitation,weather_code,cloud_cover"
    
    response = requests.get(url, verify=False)  # Open link, verify=False to ignore SSL warnings
    data = response.json()  # Convert to JSON

    # Extract relevant data
    current_is_day = data["current"].get("is_day", None)
    current_time = data["current"].get("time", None)
    current_precipitation_status = data["current"].get("precipitation", None)
    current_overall_status = data["current"].get("weather_code", None)


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


