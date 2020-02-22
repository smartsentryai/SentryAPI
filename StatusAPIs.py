import requests
import json


class StatusAPIs:

    def __init__(self, sentry_id, camera, API_KEY, url):
        self.headers = {
            'content-type': "application/json",
            'x-api-key': API_KEY,
            'cache-control': "no-cache"
        }
        self.url = url
        self.sentry_id = sentry_id
        self.camera = camera
        self.payload = {'sentry_id': sentry_id, "camera_information": ""}

    def get_results_for_status_api(self):
        self.url += "?sentry_id=" + self.sentry_id + "&camera=" + camera
        response = requests.request("GET", self.url, headers=self.headers, timeout=25)
        return response

    def update_payload(self, camera_id, camera_response):
        cam_info = {camera_id: camera_response}
        self.payload.update({"camera_information": cam_info})

    def post_response_for_status_api(self):
        response = requests.request("POST", self.url, data=json.dumps(self.payload), headers=self.headers, timeout=25)
        return response

    def parse_output_post(self, response):
        output = json.loads(response.text)
        status_code = output["statusCode"]
        if status_code is 200:
            print("Updated Successfully")
        elif status_code is 400:
            print("Update failed. Retry update.")

    def parse_get_output(self, response):
        output = json.loads(response.text)
        marketing_message = output["marketing_message"]
        marketing_url = output["marketing_url"]
        marketing_url_name = output["marketing_url_name"]
        print("Marketing Message = ", marketing_message)
        print("Marketing URL to subscribe to sentry = ", marketing_url)
        print("Marketing URL Name = ", marketing_url_name )

        trial_license = output['trial_license']
        paid_license = output["paid_license"]
        if paid_license is True:
            print("This is paid sentry_id")
        else:
            print("This is not a paid sentry_id")

        if trial_license is "active":
            print("The sentry_id is in trial phase")
        elif trial_license is "expired":
            print("The trial for sentry_id has expired")
        else:
            print("This is an inactive sentry_id")

        camera_information = output["camera_information"]
        for i in camera_information:
            if camera_information[i]["person"] is True:
                print("Person detection is on")
            else:
                print("Person detection is off")
            if camera_information[i]["face"] is True:
                print("Face ID is on")
            else:
                print("Face ID is off")

        # Times to send images in milliseconds since motion event trigger
        first_image_time = output["first_image_time"]
        second_image_time = output["second_image_time"]
        third_image_time = output["third_image_time"]

        print("First image delay after motion trigger = ", first_image_time)
        print("Second image delay = ", second_image_time)
        print("Third image delay = ", third_image_time)


if __name__ == '__main__':
    # Get it from Sentry
    sentry_id = ''
    camera = 'Cam1'
    API_KEY = ""
    URL = "https://api.smartsentry.ai/v2/status"

    api_object = StatusAPIs(sentry_id, camera, API_KEY, URL)

    '''
    The Status() Request call is to keep camera settings synchronized between our 
    Application integrations and the Sentry cloud.  
    To that end, the common usage for Status() calls are:
        - At application startup.  It's always good to make sure the internal configuration 
            is consistent with Sentry AI settings.  
        - Calling Status() at startup also results in synchronization whenever the application 
            is reinstalled after a hardware crash or installed on another machine.
    '''
    result = api_object.get_results_for_status_api()
    api_object.parse_get_output(result)

    '''
    The Status() Post call is to turn settings on/off.  Similar to before, 
    if the user activates the person detection and/or face id checkbox, when closing the dialog, 
    send the status post call in order to activate or deactivate a feature. 
    '''
    res = {"person": True, "face": True}
    camera_id = sentry_id+"_"+camera
    api_object.update_payload(camera_id, res)
    post_result = api_object.post_response_for_status_api()
    api_object.parse_output_post(post_result)

