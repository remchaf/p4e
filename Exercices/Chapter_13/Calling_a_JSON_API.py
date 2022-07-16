import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = {}
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
        # print(json.dumps(js, indent=3))
    except:
        print('==== Failure To Retrieve ====')
        continue

    if js["status"] == "OK" :
        latitude = js['results'][0]['geometry']['location']['lat']
        longitude = js['results'][0]['geometry']['location']['lng']
        print('latitude', latitude, 'longitude', longitude)
        location = js['results'][0]['formatted_address']
        print(location)
        print("Place_id :", js["results"][0]["place_id"])
    else : continue