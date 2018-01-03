import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv

app = Flask(__name__)

DATABASE = []

def returnAllCSV():
	return glob.glob( 'datapoints/*.csv' )

def readCSVs():
	for csvFile in returnAllCSV():
		with open(csvFile, 'rb') as f:
			reader = csv.reader(f)
			your_list = list(reader)
			for your_listz in your_list:
				try:
					DATABASE.append({"Bus": your_listz[0], "Lat": your_listz[1], "Long": your_listz[2]})
				except:
					pass

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", DATABASE=DATABASE)

if __name__ == "__main__":
	readCSVs()
	app.run(host='0.0.0.0', port=8888)