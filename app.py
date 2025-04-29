from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This will render the 'index.html' file located in the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    # Set host to '0.0.0.0' to allow access via a custom IP address or external interface
    app.run(host='0.0.0.0', port=5000, debug=True)

import requests

#Hide warnings ----
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#------------------

def index():
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.8041&longitude=-93.1669&hourly=soil_moisture_1_to_3cm,soil_temperature_6cm&current=temperature_2m,is_day,showers,snowfall,rain,precipitation,weather_code,cloud_cover"
    response = requests.get(url, verify=False)
    data = response.json()

    # Get the "is_day" data (whether it's daytime or not)
    is_day_data = data["current"].get("is_day", None)

    # Pass the data to the HTML page
    return render_template("index.html", is_day=is_day_data)

if __name__ == '__main__':
    app.run(debug=True)



index()