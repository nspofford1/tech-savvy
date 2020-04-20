import urllib.request
import urllib.parse
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "R3HyBIdzjniINxFFjt79uIEKezAUZ8rR"
MBTA_API_KEY = "4b4f64b27f2a4c6ba26da48d7513b9b7"

# A little bit of scaffolding if you want to use it

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'

#We don't really need to print all of the get JSON response data since it contains too much information, most of which is not relevant. We only need the latitude, longitude for a place, in this case, Babson College. 

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    MAPQUEST_API_KEY= 'R3HyBIdzjniINxFFjt79uIEKezAUZ8rR'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place = place_name.replace(' ', '%20')
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place}'
    # print(url) # uncomment to test the url in browser
    place_json = get_json(url)
    # pprint(response_data)- we don't need to show all the data
    lat = place_json["results"][0]["locations"][0]['displayLatLng']['lat']
    lon = place_json["results"][0]["locations"][0]['displayLatLng']['lng']
    return lat, lon


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    # print(url) # uncomment to test the url in browser
    station_json = get_json(url)
    station_name = station_json["data"][0]["attributes"]['name']
    wheelchair_boarding = station_json["data"][0]["attributes"]['wheelchair_boarding']
    if wheelchair_boarding == 2:
        wheelchair_boarding = 'Inaccessible'
    elif wheelchair_boarding == 1:
        wheelchair_boarding = 'Accessible'
    else:
        wheelchair_boarding = 'No Information'
    return station_name, wheelchair_boarding

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    return get_nearest_station(*get_lat_long(place_name))

def main():
    # final test here
    place = input('Enter a place name in Boston such as "Fenway Park": ')
    lat, lon = get_lat_long(place)
    print(lat, lon)
    print(get_nearest_station(lat, lon))

    # final wrap-up
    print(find_stop_near(place))
    
if __name__ == '__main__':
    main()