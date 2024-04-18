"""
This code is to test the functionality of the location class
and impelment this into the frontend.
"""

from flask import Flask, render_template, request, jsonify
import geocoder
import googlemaps
import folium
import location


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

@app.route('/display_distance', methods=['POST'])
# Function to display the closest dining hall on a map
def display_closest_dining_hall():
    closest_dining_hall = location.find_closest_dining_hall()
    user_location = location.find_student_location()
    if closest_dining_hall:
        # Create a map centered at the user's location
        map_center = [user_location[0], user_location[1]]
        map_student_to_dining_hall = folium.Map(location=map_center, zoom_start=15)

        # Add a marker for the student's location
        folium.Marker(location=map_center, popup="Student's Location", icon=folium.Icon(color="blue")).add_to(map_student_to_dining_hall)

        # Add a marker for the nearest dining hall
        dining_hall_location = [closest_dining_hall[0], closest_dining_hall[1]]
        folium.Marker(location=dining_hall_location, popup=closest_dining_hall["name"]).add_to(map_student_to_dining_hall)

        # Get walking directions
        walking_directions = location.get_walking_directions(user_location, closest_dining_hall)

        # Add polyline for walking directions
        folium.PolyLine(locations=folium.PolyLine.decode(walking_directions), color="red").add_to(map_student_to_dining_hall)

        # Display the map
        map_student_to_dining_hall.save("student_to_dining_hall_map.html")
        print("Map generated successfully. Please open 'student_to_dining_hall_map.html' to view the route.")

    else:
        print("No dining halls found.")
