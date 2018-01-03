import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv

app = Flask(__name__)

DATABASE = []
BUSNUM = raw_input("Bus Number: ")

def returnAllCSV(busNum):
	return glob.glob('datapoints/{}.csv'.format(busNum))

def readCSVs():
	for csvFile in returnAllCSV(BUSNUM):
		with open(csvFile, 'rb') as f:
			reader = csv.reader(f)
			your_list = list(reader)
			for your_listz in your_list[:100000]:
				try:
					DATABASE.append({"Lat": your_listz[2], "Long": your_listz[1]})
				except Exception as exp:
					print exp
					pass

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", DATABASE=DATABASE, BUSNUM=BUSNUM)

if __name__ == "__main__":
	readCSVs()
	DATABASE = [dict(t) for t in set([tuple(d.items()) for d in DATABASE])]
	print(len(DATABASE))
	app.run(host='0.0.0.0', port=8888)