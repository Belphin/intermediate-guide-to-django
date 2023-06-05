


def set_default_keys(dict, keys):
	data = dict.copy()
	for key in keys:
		if not key in dict:
			data[key] = keys[key]
	return data