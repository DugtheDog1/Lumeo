from flask import Flask, render_template, request
import requests
from datetime import datetime
import pytz

app = Flask(__name__, static_folder='Static')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


def weather():
    # Your location
    latitude = 44.98
    longitude = -93.27

    # Build the API request URL
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=precipitation,temperature_2m"
        f"&daily=sunrise,sunset"
        f"&timezone=auto"
    )

    # Fetch the data
    response = requests.get(url)
    data = response.json()

    # Extract values
    precip_mm = data["current"]["precipitation"]
    precipitation = precip_mm > 0

    temperature_celsius = data["current"]["temperature_2m"]
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32

    timezone_str = data["timezone"]
    sunrise_str = data["daily"]["sunrise"][0]
    sunset_str = data["daily"]["sunset"][0]

    # Convert sunrise/sunset to datetime objects
    sunrise = datetime.fromisoformat(sunrise_str).replace(tzinfo=pytz.timezone(timezone_str))
    sunset = datetime.fromisoformat(sunset_str).replace(tzinfo=pytz.timezone(timezone_str))

    # Get current time in the same timezone
    local_tz = pytz.timezone(timezone_str)
    now = datetime.now(local_tz)

    # Check if the current time is between sunset and sunrise
    lights_on = False
    if now > sunset or now < sunrise:
        lights_on = True

    # Log the current time and lights_on status
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    if lights_on:
        print("lights_on: TRUE")
    else:
        print("lights_on: FALSE")

    # Handle form submission
    if request.method == 'POST':
        # Check if action key exists before accessing it
        action = request.form.get('action')

        if action == 'turn_off':
            print("Lights: Shut Off")
        elif action == 'turn_on':
            print("Lights: Turn On")
        elif action == 'set_color':
            color = request.form['color']
            print(f"Lights: Set Color to {color}")
    
    # Return the rendered template with weather data
    return render_template('index.html', 
                           current_time=now.strftime('%Y-%m-%d %H:%M:%S'),
                           timezone=timezone_str,
                           precipitation=precipitation,
                           precip_mm=precip_mm,
                           temperature_celsius=temperature_celsius,
                           temperature_fahrenheit=temperature_fahrenheit,
                           sunrise=sunrise.strftime('%H:%M:%S'),
                           sunset=sunset.strftime('%H:%M:%S'))

if __name__ == "__main__":
    app.run(debug=True)