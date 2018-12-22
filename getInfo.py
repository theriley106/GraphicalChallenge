import json

def all():
	# Returns all info
	return json.load(open("info.json"))
