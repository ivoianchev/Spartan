import os
import re
import json

# custom libs
from spartan.utils import cache
from spartan.utils import jsonloader
from spartan.utils import settings
from spartan.utils.log import log


# get all text snippets from the json file
def get_snippets(json_data):
	snippets = []

	# add as t1 => snippet
	i = 1
	for snippet in json_data:
		trigger = "t" + str(i)
		
		snippets.append((trigger, snippet))

		i += 1

	# add as text(no spaces) => snippet
	for snippet in json_data:
		trigger = re.sub('[^0-9a-zA-Z]+', '', snippet)

		snippets.append((trigger, snippet))

	return snippets


def get_emmet_snippets(json_data):
	snippets = {}

	# add as t1 => snippet
	i = 1
	for snippet in json_data:
		trigger = "t" + str(i)
		
		snippets[trigger] = snippet

		i += 1

	return snippets


def export_to_emmet(json_data):
	emmet_snippets = get_emmet_snippets(json_data)

	json_raw_data = {
		"html": {
			"snippets": {}
		},

		"spartantextsnippets": {}
	}

	json_raw_data['html']['snippets'] = emmet_snippets;
	json_raw_data['spartantextsnippets'] = emmet_snippets;

	# save the file
	file_path = settings.get('emmet_snippets_file_path')

	with open(file_path, 'w') as outfile:
  		json.dump(json_raw_data, outfile)



# get the text snippets from the json or from the cache
def load(view):

	# get the json file
	json_file = settings.get("text_snippets_file_path")
	log("json_file: " + json_file)

	# check if this is real file
	if not os.path.isfile(json_file):
		log("Error -- not a file")
		return []

	# get the modification time
	current_modify_time = os.path.getmtime(json_file)

	# check if we have this already cached
	cached_snippets = cache.get("text_snippets", current_modify_time)

	if cached_snippets : 
		log("loaded from cache")
		return cached_snippets

	# nothing cached - get the json data
	json_data = jsonloader.load_file(json_file)

	# get all text snippets
	text_snippets = get_snippets(json_data)

	# cache the snippets
	cache.add("text_snippets", text_snippets, current_modify_time)

	# export to emmet
	export_to_emmet(json_data)

	# reload emmet
	view.run_command("emmet_reset_context")
	
	log("loaded from json")

	return text_snippets