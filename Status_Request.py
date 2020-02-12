import requests

sentry_id = "R6GNAS-B"
API_KEY = ""

url = "https://api.smartsentry.ai/v2/status?sentry_id="+sentry_id

headers = {
 'x-api-key': API_KEY,
 'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers)

print(response.text)

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
