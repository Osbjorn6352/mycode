#!/usr/bin/python3
import requests
import pprint

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startDateInp = input("Please enter a start date(in the format YYYY-MM-DD) from which to explore NEOs\n> ")
    startdate = f"start_date={startDateInp}"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    fullUrl = NEOURL + startdate + "&" + nasacreds
    neowrequest = requests.get(fullUrl)
    print(fullUrl)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    ## pprint.pprint(neodata)

    datesDict = neodata['near_earth_objects']
    sentryObjects = []

    for date in datesDict:
        for obj in range(len(datesDict[date])):
            objName = datesDict[date][obj]['name']
            isSentry = datesDict[date][obj]['is_sentry_object']
            if isSentry == True:
                readable = objName + " is a sentry object and was listed close to earth on " + date
                sentryObjects.append(readable)

    if len(sentryObjects) == 0:
        print("There are no sentry objects from your specified date")

    else:
        for neo in sentryObjects:
            print(neo)

    diameterList = []
    proximityList = []
    largestObj = ''
    closestObj = ''
    for date in datesDict:
        for objIndex in range(len(datesDict[date])):
            objName = datesDict[date][objIndex]['name']
            diameter = datesDict[date][objIndex]['estimated_diameter']['meters']['estimated_diameter_max']
            proximity = datesDict[date][objIndex]['close_approach_data'][0]['miss_distance']['miles']
            diameterList.append(diameter)
            proximityList.append(proximity)
    largest = max(diameterList)
    closest = min(proximityList)

    print(f"The largest NEO from your selected date has a max estimated diameter of {diameter} meters.")
    print(f"The closest approach from an NEO came a mere {proximity} miles from Earth!")

if __name__ == "__main__":
    main()

