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
commons_address = '1969 Burdett Ave, Troy, NY'