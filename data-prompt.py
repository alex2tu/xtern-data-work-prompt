import json

import folium
import requests
from googleplaces import GooglePlaces, lang, types

API_KEY = 'enter API key here'

def get_places(location, searchRadius):
    res = []
    coords = location.split(",")
    #fetch hospitals around location logic implemented from geeksforgeeks
    #https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/
    google_places = GooglePlaces(API_KEY) 
    query_result = google_places.nearby_search( 
        lat_lng ={'lat': float(coords[0]), 'lng': float(coords[1])}, 
        radius = searchRadius, 
        # types =[types.TYPE_HOSPITAL] or 
        # [types.TYPE_CAFE] or [type.TYPE_BAR] 
        # or [type.TYPE_CASINO]) 
        types =[types.TYPE_MEAL_DELIVERY]) 
    for place in query_result.places: 
        # print(place) 
        # print (place.name) 
        # print("Latitude", place.geo_location['lat']) 
        # print("Longitude", place.geo_location['lng']) 
        # print()
        res.append(place)

    return res

def draw_places(map,places):
    for place in places:
        # print("test")
        name = place.name
        lat = place.geo_location['lat']
        lng = place.geo_location['lng']
        folium.Marker([lat, lng], popup=name).add_to(map)

def main():
    #locations with coords
    indianapolisIN = "39.7684,-86.148003"
    westLafayetteIN = "40.425869, -86.908066"

    #initialize params
    location = indianapolisIN
    radius = 5000

    m = folium.Map(location=[float(coord) for coord in location.split(",")], zoom_start=15)

    places = get_places(location,radius)
    #call method to find places (hospitals for now to test) near coordinates
    draw_places(m,places)

    #marked map with hospitals for now
    m.save("map.html")

if __name__ == "__main__":
    main()
