import requests
import json

API_KEY = ""
url = "https://api.smartsentry.ai/v2/status?sentry_id=5FBUD6-B"

input_body = {
   "sentry_id": "5FBUD6-B",
   "camera_information": {
       "5FBUD6-B_Cam1": {"person": True, "face": True},
       "5FBUD6-B_chip_test_cam": {"person": True, "face": True}
   }
}

payload = json.dumps(input_body)
headers = {
 'x-api-key': API_KEY,
 'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
