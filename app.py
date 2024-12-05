from flask import Flask, render_template, request, jsonify
import requests
import os
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    return render_template('index.html', weather=weather_data)

@app.route('/forecast', methods=['POST'])
def forecast():
    city = request.form['city']
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    forecast_data = response.json()
    return render_template('index.html', forecast=forecast_data)

@app.route('/geolocation', methods=['POST'])
def geolocation():
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(request.form['location'])
    if location:
        return jsonify({'latitude': location.latitude, 'longitude': location.longitude})
    else:
        return jsonify({'error': 'Location not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
