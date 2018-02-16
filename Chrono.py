import googlemaps
import config
from datetime import datetime as dt

gmaps = googlemaps.Client(key=api_key)

now = dt.now()

directions_result = gmaps.directions("Tucson, AZ","Phoenix, AZ",mode="transit", departure_time=now)

print (directions_result)
