#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
responseDict = response.json()
responseLon = responseDict['iss_position']['longitude']
responseLat = responseDict['iss_position']['latitude']
coordsTuple = (responseLat, responseLon)

def epochToStandard(epochTime):
    unformatted = datetime.datetime.fromtimestamp(epochTime)
    formatted = unformatted.strftime('%Y-%m-%d / %H:%M:%S')
    print(formatted)

def revGeocode(coords):
    result = rg.search(coordsTuple, verbose=False)
    airspaceCity = result[0]['name']
    airspaceCountry = result[0]['cc']
    print(airspaceCity + ',', airspaceCountry)

if __name__ == '__main__':
    print("CURRENT ISS POSITION IN LATITUDE AND LONGITUDE:")
    print(f"LON: {responseDict['iss_position']['longitude']}")
    print(f"LAT: {responseDict['iss_position']['latitude']}")

    revGeocode(coordsTuple)
    epochToStandard(responseDict['timestamp'])

