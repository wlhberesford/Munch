"""
To test this method you would need to install geocoder
by doing the following command in your terminal:
pip install geocoder
pip install -U googlemaps
"""

"""
How to get distance: 
1. Get latitude and longitude of two addresses using Geocoder library
        a. user location
        b. each dining hall location
2. Use Google Maps Distance Matrix API to calculate the walking time between these two addresses
3. display the closest dining hall from the users current location
"""

import csv
import pandas as pd
import googlemaps

import url
import requests

import geocoder
import folium


sage_address = '1649 15th St, Troy, NY'
barh_address = '100 Albright Ct, Troy, NY'
blitman_address = '1800 6th Ave, Troy, NY'
commons_address = '1969 Burdett Ave, Troy, NY'


def find_student_location():
    try:
        student_location = geocoder.ip("me")
        if student_location.ok:
            student_lat, student_long = student_location.latlng
        else: 
            raise Exception('Unable to get location of user')
    except Exception as e:
        raise SystemError(f"Could not get student's IP address: {e}")
    return (student_lat, student_long)



# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def find_address_location(address):
    # Use geocoder to get the location of the address
    try: 
        location = geocoder.google(address, key='YOUR_API_KEY')
        if location.ok:
            address_lat, address_long = student_location.latlng
        else:
            raise Exception('Unable to get location of address')
    except Exception as e:
        raise SystemError(f"Could not get Address's IP address: {e}")
    return (address_lat, address_long)
    

def calculate_walking_time(origin, destination):
    # Use Google Maps Distance Matrix API to calculate the walking time
    try: 
        matrix = gmaps.distance_matrix(origin, destination, mode='walking')
        if matrix['status'] == 'OK':
            total_distance, total_duration = 0
            for step in directions[0]['legs'][0]['steps']:
                total_distance += step['distance']['text']
                total_duration += step['duration']['text']
        else:
            raise Exception('Unable to calculate walking time')
    except Exception as e:
        raise SystemError(f"Google Maps API request failed: {e}")
    return (total_distance, total_duration)


def find_closest_locations():
    student_location = find_student_location()
    sage_location = find_address_location(sage_address)
    barh_location = find_address_location(barh_address)
    blitman_location = find_address_location(blitman_address)
    commons_location = find_address_location(commons_address)
    
    # Get the locations of the student and the dining hall
    sage_time = calculate_walking_time(student_location, sage_location)
    barh_time = calculate_walking_time(student_location, barh_location)
    blitman_time = calculate_walking_time(student_location, blitman_location)
    commons_time = calculate_walking_time(student_location, commons_location)
    
    total = [sage_time, barh_time, blitman_time, commons_time]
    total.sort()
    
    # Return the closest one that is within a reasonable distance
    if total[0] == sage_time:
        return sage_location
    if total[0] == barh_time:
        return barh_location
    if total[0] == blitman_time:
        return blitman_location
    if total[0] == commons_time:
        return commons_location


def display_closest_dining_hall():
    closest_dining_hall = find_closest_locations()
    user_location = find_student_location
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
        walking_directions = get_walking_directions(user_location, closest_dining_hall)

        # Add polyline for walking directions
        folium.PolyLine(locations=folium.PolyLine.decode(walking_directions), color="red").add_to(map_student_to_dining_hall)

        # Display the map
        map_student_to_dining_hall.save("student_to_dining_hall_map.html")
        print("Map generated successfully. Please open 'student_to_dining_hall_map.html' to view the route.")

    else:
        print("No dining halls found.")

def get_walking_directions(user, dining):
    # Make a request to Google Maps Directions API
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "mode": "walking",  # Specify walking mode
        "key": "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your Google Maps API key
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Parse the response and extract the polyline points
    polyline_points = data["routes"][0]["overview_polyline"]["points"]
    return polyline_points