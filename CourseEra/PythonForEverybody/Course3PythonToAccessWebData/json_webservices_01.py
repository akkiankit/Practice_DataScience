import urllib.request,urllib.response,urllib.parse,urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input("enter location:")
    
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({'address' : address}) 

    print("retriving ...", url)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrived ", len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print("********Failur  to Retrieve *******")
        print(data)
        continue

    lat = js['results'][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("latitude",lat, "longitude",lng)

    location  = js["results"][0]["formatted_address"]
    print(location)
