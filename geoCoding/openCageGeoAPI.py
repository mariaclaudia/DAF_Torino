import sys
from opencage.geocoder import OpenCageGeocode

key = 'YouAPI'
geocoder = OpenCageGeocode(key)
infilepath = 'indirizzi.txt'

try: 
  with open(infilepath,'r') as f:
    for line in f:
      address = line.strip()
      query = address;
      result = geocoder.geocode(query)

      if result and len(result):
        longitude = result[0]['geometry']['lng']
        latitude  = result[0]["geometry"]["lat"]
        z = "%f;%f;%s" % (latitude, longitude, query)
        print z
      else:
        sys.stderr.write("not found: %s\n" % query)
except IOError:
  print("Error: File does not appear to exist.")