# all cashe
cache = {}


# add object in cache
def add(name, snippets, time):
	cache[name] = {
		'modify_time': time,
		'snippets': snippets,
	}

	return


# get object from the cache
def get(name, time):
	cache = globals()['cache']

	# check if we have such snippets in our cache
	if not cache.has_key(name) : 
		return False

	snippets_cache = cache[name]

	# check if we have modification time
	if not snippets_cache.has_key('modify_time') :
		return False

	# check if we have snippets
	if not snippets_cache.has_key('snippets') : 
		return False

	if snippets_cache['modify_time'] != time : 
		return False

	return snippets_cache['snippets']


