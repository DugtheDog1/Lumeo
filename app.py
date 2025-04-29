from flask import Flask, render_template
import requests

app = Flask(__name__)

# Hide warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@app.route('/')
def home():
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.8041&longitude=-93.1669&hourly=soil_moisture_1_to_3cm,soil_temperature_6cm&current=temperature_2m,is_day,showers,snowfall,rain,precipitation,weather_code,cloud_cover"
    
    response = requests.get(url, verify=False) #Open link, verify is false due to the thing and the import urllib3 and .disable_warnings is to ignore the message
    data = response.json() # Convert to json 

    is_day_data = data["current"].get("is_day", None) #Goes through the data and looks for current/is_day value in dictionary thing

    return render_template("index.html", is_day=is_day_data) #Think global var, exports data to the html page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
