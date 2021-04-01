### Sentry API Example


##### Explanation of changes for BI:

* Area of motion is a list of bounding boxes showing where the motion or motions occurred in the image. This will improve our detection accuracy.
* Occupied state has changed. Three states are sent in the field; Alert, Occupied and Vacant. 
* Person bounding boxes are sent whenever a person is found, even if the state is Occupied. (This was not the case in the previous version.) "Alert" is sent when a person or people appear when the state was Vacant. 
* The intent is to send alerts on "Alert", and not send alerts and show the reason as Occupied when the state field returns "Occupied".
* The support for new feature, i.e, Vehicle Detection is added with two Boolean variables, which can be changed independently using /registration API request
* Added the Version Information

***
#### Sample Registration Request:
The Registration request will be extended to include the Person and Vehicle detection features. 
This API will create a new Sentry ID (Site ID) if the attribute is not present. This for handling the new customer onboarding. 
If it exists, it will update the feature options and send the result back accordingly.

    {
        'body': {
            'partner_identifier': <Same as before>, 
            'company_name': <Same as before>
            'Site_Id' : <Sentry ID/Site ID, if it already exists. If not, not needed to send this attribute>
        }
    }

***
#### Sample Registration Response:
Will keep the response format same as before, to keep it compatible with old Blue Iris.

    Code: 200
    {
        Sentry_Id: ‘ABCDEFGH-P’  
    }

***
##### Sample POST Request:


With Area of Motion and Image and Event Timestamps:

    {
        'body': {
            'Site_Id': '5FBUD6-B', 
            'Camera_Name': 'Cam1', 
            'Area_Of_Motion': [[44,34,56,21]],
            'Image_Timestamp': 11582390157999, # Linux epoch time in milliseconds.
            'Motion_Event_Timestamp': 11582390156999,
            'person': 'true',  # true or false
            'vehicle' : 'true'   # true or false,
            'Image_Bytes': "/9j/2wCEAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDIBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAZABkAMBIgACEQEDEQH/xAGiAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgsQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+gEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoLEQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RUQlmCgdycV89fFmTTZ/E5ew2Z8sCZkHBcZ/pisSbxXqs0ex7+4ZT2MhrDubhpmJckknqTXCp1Jtcysd………………………………………."
        }
    }



***

##### Sample Response:
The **vehicle_results** will be included in the response if/when applicable. This is to make sure that we have backward compatibility.

    {
        'marketing_message': 'SIGN UP AT Smartsentry.ai/register TO RECEIVE YOUR  CAMERA(S) DAILY SMART REPORT.', 
        'person_results': {
            'bounding_box': [[41, 2, 1360, 908]], 
            'occupied_state': 'Alert'
        }      
        'vehicle_results': {
            'vehicle_bounding_boxes': [[12,243,123,454]],
            'vehicle_occupied_state': 'Alert'
        }
    }
    
    
##### Status APIs:
******************

GET - The Status() Request call is to keep camera settings synchronized between our Application integrations and the Sentry cloud. To that end, the common usage for Status() calls are:
  * At application startup.  It's always good to make sure the internal configuration is consistent with Sentry AI settings.
  * Calling Status() at startup also results in synchronization whenever the application is reinstalled after a hardware crash or installed on another machine.

##### query parameters sentry_id, camera
https://api.smartsentry.ai/v2/status?sentry_id=5FBUD6-B&camera=Cam1

##### Sample Response - 

    {
        "trial_license": "active",
        "paid_license": false,
        "marketing_message": "Thanks for using Sentry alerts!",
        "marketing_url": "https://www.smartsentry.ai/sentry-smart-alert?sentry_id=5FBUD6-B",
        "marketing_url_name": "Learn more about Sentry AI.",
        "camera_information": {
            "5FBUD6-B_Cam1": {
                "person": true, # true or false, based on the last image status
                "vehicle": true. #true or false, based on last image status
            }
        }
    }
    
*******************



