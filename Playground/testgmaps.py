import googlemaps
import API_KEY

gmaps = googlemaps.Client(API_KEY.api_key)
geocode_result = gmaps.geocode("Calle de la Torrecilla del Leal, 12")
if geocode_result and len(geocode_result) > 0:
    lat = geocode_result[0]['geometry']['location']['lat']
    lon = geocode_result[0]['geometry']['location']['lng']
    
print(lat, lon)