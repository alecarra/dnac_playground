# dnac_playground
# these are the files that we'll be using during brkdev-1105 in Cisco Live Cancun 2019

Cisco Live Cancun 19.postman_collection.json	--> Has the colleciton of the API's we'll be showing. you need to change the username/password
device_list.json	 --> Contains a list of network devices from Alex's lab, use this file if you want to run embedded_filename.py
embedded_filename.py	--> Will ask you for the device_list.json file to parse the data
env_lab_brk_1105.py	First --> Will get you the authentication token
get_dnac_devices.py	First --> will automate the login to Cisco DNA Center and parse the inventory with the information that we need
