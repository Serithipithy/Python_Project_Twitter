"""Google Maps Service

This script converts the location given as a string( Ex: 'Iasi, Romania')
into coordinates (longitude and latitude)

This tool accepts addresses

This file can also be imported as a module and contains the following
functions:

    * get_coordinates - converts an address into coordinates
"""
from geopy.geocoders import Nominatim


def get_coordinates(address):
    """
    Converts an address into coordinates
    :param address:
        the address that has to be converted
    :return: list
        the coordinates as a vector of 2 elements
        by default it returns [0,0] if the location doesn't exist
    """
    if len(address) > 0:
        geolocator = Nominatim(user_agent="Alexandraa")
        location = geolocator.geocode(address, timeout=None)
        if location:
            return [location.latitude, location.longitude]
    return [0, 0]
