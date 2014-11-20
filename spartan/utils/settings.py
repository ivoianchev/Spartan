import sublime
import os

# JSON File names
text_snippets_file = 'text-snippets.json'
css_snippets_file = 'css-snippets.json'


# Load ST User settings
settings = sublime.load_settings('Spartan.sublime-settings')


# Get settings
def get( setting ) :
	if setting == 'json_location' :
		return get_json_location()

	elif setting == 'text_snippets_file_path' : 
		return get_json_file_path( text_snippets_file )

	elif setting == 'css_snippets_file_path' :
		return get_json_file_path( css_snippets_file )

	return settings.get( setting )


# Get json location - returns c:\users\%username\.spartan\ if its not set
def get_json_location():
	if settings.get('json_location'):
		return settings.get('json_location')

	# return the default path
	return os.path.expanduser('~') + '\\' + '.spartan\\'


# Get json file full path
def get_json_file_path( file_name ):
	return get_json_location() + file_name