import requests

sentry_id = "R6GNAS-B"
camera = "Cam45"
API_KEY = ""

url = "https://api.smartsentry.ai/v2/status?sentry_id=" + sentry_id

headers = {
 'x-api-key': API_KEY,
 'Content-Type': 'application/json'
}

// The status() call synchronizes Sentry AI settings with the application.  Often called at application startup.
response = requests.request("GET", url, headers=headers)

print(response.text)

// get attributes for camera
<madhurya, write code to parse response to get Cam45 attributes>

if (person == true)
    print("Person detection is on")
else
    print("Person detection is off"
          
if (face == true)
    print("Face ID is on")
else
    print("Face ID is off")

          
// The status call is also used to determine active services based on license status
<madhurya right appropriate logic similar to above explaining what to do with trial and paid licenses>

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
