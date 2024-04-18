"""
This code is to test the functionality of the location class
and impelment this into the frontend.
"""

from flask import Flask, render_template, request, jsonify
import geocoder
import googlemaps

app = Flask(__name__)

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_distance', methods=['POST'])
def calculate_distance():
    location1 = request.form['location1']
    location2 = request.form['location2']
    distance = haversineDistance(location1, location2)
    return jsonify({'distance': distance})