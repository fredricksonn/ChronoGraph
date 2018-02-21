import googlemaps
import urllib
import config
import json

places_query=['McDonalds','Walmart','OReilly Auto Parts','Taco Bell']
places_radius='40000' #meters, ~25 miles
places_location='32.2217,-110.9265' #Tucson Coordinates
places_formatted_addresses = []

### SET URL FOR REQUEST ###
places_endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
places_options_req = '&location={}&radius={}'.format(places_location,places_radius)

for place in places_query:
	places_req = 'query={}&key={}'.format(place,config.api_key)
	places_request = places_endpoint + places_req + places_options_req

	### SEND REQUEST AND CATCH RESPONSE ###
	places_response = urllib.urlopen(places_request).read()

	### INTERPRET DATA INTO PYTHON TYPES ###
	places_list = json.loads(places_response)

	### UNCOMMENT TO PRINT FULL FORMATTED OUTPUT ###
	#print(json.dumps(places_list, sort_keys=False, indent=4))

	results = places_list['results']
	for result in results:
		places_formatted_addresses.append(result['formatted_address'])

print (places_formatted_addresses)
	
