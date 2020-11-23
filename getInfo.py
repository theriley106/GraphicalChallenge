import json

def all():
	# Returns all info
	return json.load(open("info.json"))

if __name__ == '__main__':
	print(all())
