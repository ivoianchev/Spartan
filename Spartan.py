import sublime
import sublime_plugin
import re
import sys
import imp


# Make sure all dependencies are reloaded on upgrade / on save
if 'spartan.utils.reloader' in sys.modules:
	imp.reload(sys.modules['spartan.utils.reloader'])
import spartan.utils.reloader


# Import custom libs
from spartan.utils import settings
from spartan.snippets import text as text_snippets


# Text snippets auto complete event 
class SpartanTextAutoComplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):

		# text snippets are only available in html context or in debug mode (check settings)
		if not view.match_selector(locations[0], 'text.html') and not settings.get("debug") :
			return []
		
		# get all text snippets
		snippets = text_snippets.load()

		return (snippets, sublime.INHIBIT_EXPLICIT_COMPLETIONS)