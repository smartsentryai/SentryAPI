import requests

sentry_id = "R6GNAS-B"
camera = "Cam45"

API_KEY = ""

url = "https://api.smartsentry.ai/v2/status?sentry_id=" + sentry_id

headers = {
 'x-api-key': API_KEY,
 'Content-Type': 'application/json'
}

// Call the status() function when starting the application in order to make sure settings are consistent with Sentry AI settings.
// If user moves the application to a different machine, the status function allows the application to know the current settings.
response = requests.request("GET", url, headers=headers)

// code to get attributes for R6GNAS-B_Cam45


// code to determine whether person identification is on for R6GNAS-B_Cam45
if (person == "true")
    print ("Person Identification is on")
 else
     print ("Person Identification is off")

// code to determine whether face id is on for R6GNAS-B_Cam45
if (face == "true")
    print ("Person Identification is on")
 else
     print ("Person Identification is off")

'''
Sample Response:
---------------
{"trial_license": "active", 
"paid_license": false, 
"marketing_message": "Thanks for using Sentry alerts!", 
"marketing_url": "https://www.smarthomesentry.com/sentry-smart-alert?sentry_id=R6GNAS-B", 
"marketing_url_name": "Learn more about Sentry AI.", 
"camera_information": {
            "R6GNAS-B_Cam45": {"person": true, "face": false}, 
            "R6GNAS-B_Cam13": {"person": false, "face": true}}
        }

'''
