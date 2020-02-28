# pip install these libraries if it doesn't exist
import base64
import requests
import json
import time


class SentryAPI:

	def __init__(self, site_id, camera_name, API_KEY, url):
		self.headers = {
			'content-type': "application/json",
			'x-api-key': API_KEY,
			'cache-control': "no-cache"
		}
		self.url = url
		self.payload = {'body': {'Site_Id': site_id, 'Camera_Name': camera_name, 'Image_Bytes': ""}}
		self.image = None

	def load_image(self, image_path):
		self.image = image_path

	def get_results_from_sentry(self):
		image_bytes = self.convert_image_to_payload_format()
		self.payload['body']['Image_Bytes'] = image_bytes
		response = requests.request("POST", self.url, data=json.dumps(self.payload), headers= self.headers, timeout=25)
		return response

	def convert_image_to_payload_format(self):
		with open(self.image, "rb") as img_file:
			base64_image = base64.b64encode(img_file.read())
		return base64_image.decode('utf-8')

	def update_payload_with_more_info(self, area_of_motion, image_timestamp, motion_event_timestamp):
		if area_of_motion:
			self.payload.update({'Area_Of_Motion': area_of_motion})
		if image_timestamp:
			self.payload.update({'Image_Timestamp': image_timestamp})
		if motion_event_timestamp:
			self.payload.update({'Motion_Event_Timestamp': motion_event_timestamp})

	def parse_output(self, response):
		output = json.loads(response.text)
		marketing_message = output["marketing_message"]
		face_results = output['face_results']
		face_bounding_boxes = face_results['face_bounding_boxes']
		face_labels = face_results['labels']
		category = face_results['categories']

		person_results = output['person_results']
		people_bounding_box = person_results['bounding_box']
		people_occupied_state = person_results['occupied_state']

		vehicle_bounding_boxes = []
		vehicle_occupied_state = ''
		pet_bounding_boxes = []
		pet_occupied_state = ''

		if 'vehicle_results' in output:
			vehicle_results = output['vehicle_results']
			if vehicle_results:
				print("Vehicle Info with bounding boxes and alert state")
				vehicle_bounding_boxes = vehicle_results['vehicle_bounding_boxes']
				vehicle_occupied_state = vehicle_results['vehicle_occupied_state']
		
		if 'pet_results' in output:
			pet_results = output['pet_results']
			if pet_results:
				print("Pet Info with bounding boxes and alert state")
				pet_bounding_boxes = pet_results['pet_bounding_boxes']
				pet_occupied_state = pet_results['pet_occupied_state']

		print("Marketing Message = ", marketing_message)
		
		print("Person Detection Results")

		if people_occupied_state == 'Alert':
			print("Person Bounding Boxes -> ", people_bounding_box)
			print('Send Alert')
		elif people_occupied_state == 'Occupied':
			print('Human found but already Alerted ')
		else:
			print('Vacant')
		print('----------------')

		print("Face Results")
		print("Face Bounding Boxes -> ",face_bounding_boxes)
		print("Face labels -> ",face_labels)
		print("Categories -> ", category)
		print('----------------')

		print("Vehicle Results")
		print("Vehicle Bounding Boxes -> ", vehicle_bounding_boxes)
		print("Vehicle Occupied State -> ", vehicle_occupied_state)
		print('-------------')

		print("Pet Results")
		print("Pet Bounding Boxes -> ", pet_bounding_boxes)
		print("Pet Occupied State", pet_occupied_state)


if __name__ == '__main__':

	# Get it from Sentry
	site_id = ''
	camera_name = 'Cam1'
	API_KEY = ""
	URL = "https://api.smartsentry.ai/v2/image"

	test_image = "Image/sentry_example.jpg"

	api_object = SentryAPI(site_id,camera_name, API_KEY, URL)
	area_of_motion = [[12,34,53,23]]
	api_object.load_image(test_image)

	# Unix epoch timestamp
	image_timestamp = int(time.time()*1000)
	motion_event_timestamp = image_timestamp - 1
	# OPTIONAL
	api_object.update_payload_with_more_info(area_of_motion, image_timestamp, motion_event_timestamp)

	output = api_object.get_results_from_sentry()
	api_object.parse_output(output)
