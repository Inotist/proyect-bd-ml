# Script para probar cosas de geopy

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Living Madrid")
location = geolocator.geocode("Calle del Pez, 36 Madrid")
print(location.address)

print(f"{location.latitude} {location.longitude}")