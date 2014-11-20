import json


from spartan.utils.log import log



# load the JSON file
def load_file(json_file):

	# open the file
	data_file = open(json_file)

	# try to parse it as json
	try:
		json_data = json.load(data_file)
	except Exception, e:
		log("load_json Error -- file is not json")
		return []

	return json_data