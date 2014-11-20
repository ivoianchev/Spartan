from spartan.utils.settings import settings

# logging
def log(str):
	if not settings.get('debug') :
		return

	print "SPARTAN -- " + str