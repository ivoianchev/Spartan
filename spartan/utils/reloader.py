import sys
import imp

# Dependecy reloader for Sparatan plugin
# The original idea is borrowed from Emmet and
# https://github.com/wbond/sublime_package_control/blob/master/package_control/reloader.py 

reload_mods = []
for mod in sys.modules:
	if mod.startswith('spartan') and sys.modules[mod] != None:
		reload_mods.append(mod)

mods_load_order = [
	'spartan.utils.settings',
	'spartan.utils.cache',
	'spartan.utils.log',
	'spartan.utils.jsonloader',
	'spartan.snippets.text'
]

for mod in mods_load_order:
	if mod in reload_mods:
		m = sys.modules[mod]
		if 'on_module_reload' in m.__dict__:
			m.on_module_reload()
		imp.reload(sys.modules[mod])