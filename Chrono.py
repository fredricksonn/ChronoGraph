import googlemaps
import config
import urllib
import json

### NOTES ###
#potentially use list of McDonalds, Walmart, Taco Bell, OReilly Auto Parts addresses for origins/destinations

### CREATE ORIGINS AND DESTINATIONS ###
origin = '1970 W Valencia Road, Tucson, AZ'
dest = 'S Wilmot Rd and E Broadway Blvd, Tucson'

### SET URL FOR REQUEST ###
endpoint = 'https://maps.google.com/maps/api/directions/json?'
nav_req = 'origin={}&destination={}&key={}'.format(origin,dest,config.api_key)
alternative_req = '&alternatives={}'.format('true')
request = endpoint + nav_req + alternative_req
print (request)

### SEND REQUEST AND CATCH RESPONSE ###
response = urllib.urlopen(request).read()

### INTERPRET DATA INTO PYTHON TYPES ###
directions = json.loads(response)

### UNCOMMENT TO PRINT FULL FORMATTED OUTPUT ###
#print(json.dumps(directions, sort_keys=False, indent=4))

### DISPLAY ROUTES WITH SUMMARIES, DISTANCES, AND DURATIONS ###
routes = directions['routes']
print("ROUTES")
for i in range(0,len(routes)):
    print(routes[i]['summary'])
    legs = routes[i]['legs']
    for j in range(0,len(legs)):
        print legs[j]['distance']['text']
        print legs[j]['duration']['text']
