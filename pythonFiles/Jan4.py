import glob
DATABASE = []
for val in open(glob.glob('static/Jan4.txt')[0]).read().split("\n"):
	try:
		lat, lon = str(val).split(', ')
		DATABASE.append({"Longitude": lon, "Latitude": lat})
	except:
		pass

def getDatabase():
	return DATABASE