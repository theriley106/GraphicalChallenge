from geopy.geocoders import GoogleV3
import csv
from uszipcode import ZipcodeSearchEngine
DATABASE = []
search = ZipcodeSearchEngine()

def returnLongLatFromCity(value):
	city, state = value.split(', ')
	a = search.by_city_and_state(city=city, state=state)[0]
	return a

listOfCities = []
with open('internships.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

for var in your_list:
	listOfCities.append(var[2])



for values in listOfCities:
	try:
		a = returnLongLatFromCity(values)
		DATABASE.append({"Longitude": a["Longitude"], "Latitude": a["Latitude"]})
		print (a["Longitude"], a["Latitude"])
	except:
		pass