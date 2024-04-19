"""
To test this method you would need to install geocoder
by doing the following command in your terminal:
pip install geocoder
pip install -U googlemaps
pip install requests
pip install folium
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

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

"""
The function 'find_student_location' is designed to get the latitude and longitude of the student's current location using the geocoder's IP method.

Args:
- None

Returns:
The function returns a tuple (student_lat, student_long). 
- student_lat: This is the latitude of the student's current location.
- student_long: This is the longitude of the student's current location.
"""
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


"""
The function 'find_address_location' is designed to get the latitude and longitude of a given address using the geocoder's google method.

Args:
- address: This is the address for which the location is to be found. It can be a string representing the address.

Returns:
The function returns a tuple (address_lat, address_long). 
- address_lat: This is the latitude of the given address.
- address_long: This is the longitude of the given address.
"""
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
    
"""
The function 'calculate_walking_time' is designed to calculate the total walking time and distance between two locations (origin and destination) using the Google Maps Distance Matrix API.

Args:
- origin: This is the starting point for the journey. It can be a string representing the address or coordinates.
- destination: This is the endpoint of the journey. Similar to the origin, it can be a string representing the address or coordinates.

Returns:
The function returns a tuple (total_distance, total_duration). 
- total_distance: This is the total walking distance from the origin to the destination. It's calculated by summing up the distances of all the steps in the route.
- total_duration: This is the total time it would take to walk from the origin to the destination. It's calculated by summing up the durations of all the steps in the route.
"""
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

"""
This function finds the closest dining hall to the student's location.

Args:
    None

Returns:
    tuple: A tuple containing the latitude and longitude of the closest dining hall.
"""
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

"""
This function displays the closest dining hall to the user's location on a map.

Args:
    None

Returns:
    None
"""
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

"""
This function retrieves walking directions between two points using the Google Maps Directions API.

Args:
    origin (tuple): A tuple containing the latitude and longitude of the origin.
    destination (tuple): A tuple containing the latitude and longitude of the destination.

Returns:
    str: A string representing the encoded polyline points of the route.
"""
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


"""
This function retrieves the current weather for a given location using the OpenWeatherMap API.

Args:
    location (str): The name of the location/city to get the weather for.

Returns:
    tuple: A tuple containing the main weather, description of the weather, the temperature in Fahrenheit, and the temperature in Celsius.
"""
def get_current_weather(location):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    API_KEY = 'YOUR_API_KEY'
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    # Make a GET request to the OpenWeatherMap API
    response = requests.get(BASE_URL, params={
        'q': location,
        'appid': API_KEY,
    })

    # Raise an exception if the request was unsuccessful
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}")

    # Parse the weather data from the response
    weather_data = response.json()
    main_weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']

    # Convert temperature from Kelvin to Celsius and Fahrenheit
    temp_celsius = temp - 273.15
    temp_fahrenheit = (temp - 273.15) * (9 / 5) + 32

    return main_weather, description, temp_fahrenheit, temp_celsius