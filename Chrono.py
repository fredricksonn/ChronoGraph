import googlemaps
import config
import urllib
import json

#potentially use list of McDonalds, Walmart, Taco Bell, OReilly Auto Parts addresses for origins/destinations

origin = '1970 W Valencia Road, Tucson, AZ'
dest = 'S Wilmot Rd and E Broadway Blvd, Tucson'

endpoint = 'https://maps.google.com/maps/api/directions/json?'
nav_req = 'origin={}&destination={}&key={}'.format(origin,dest,config.api_key)

request = endpoint + nav_req
response = urllib.urlopen(request).read()
directions = json.loads(response)

routes = directions['routes']
print (routes)
print("ROUTES")
for i in range(0,len(routes)):
    print(routes[i]['summary'])

    print("LEGS")
    legs = routes[i]['legs']
    print(len(legs))
    for j in range(0,len(legs)):
        print legs[j]['distance']['text']
