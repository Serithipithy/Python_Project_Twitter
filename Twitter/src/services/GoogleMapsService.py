from geopy.geocoders import Nominatim


def get_coordinates(address):
    if len(address) > 0:
        geolocator = Nominatim(user_agent="Alexandra")
        location = geolocator.geocode(address)
        return [location.latitude, location.longitude]
    return False
