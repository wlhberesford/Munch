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


def find_address_location(address):
    # Returns tuple of lat/lon for given address string
    return address