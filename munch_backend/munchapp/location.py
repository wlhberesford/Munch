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

# Get the locations of the student and the dining halls
student_location = find_student_location()
sage_location = find_address_location(sage_address)
barh_location = find_address_location(barh_address)
blitman_location = find_address_location(blitman_address)
commons_location = find_address_location(commons_address)


sage_time = calculate_walking_time(student_location, sage_location)
barh_time = calculate_walking_time(student_location, barh_location)
blitman_time = calculate_walking_time(student_location, blitman_location)
commons_time = calculate_walking_time(student_location, commons_location)

print(f"Walking time to Sage: {sage_time}")
print(f"Walking time to BARH: {barh_time}")
print(f"Walking time to Blitman: {blitman_time}")
print(f"Walking time to Commons: {commons_time}")