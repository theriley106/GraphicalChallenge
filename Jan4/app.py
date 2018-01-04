import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv
from geopy import geocoders

app = Flask(__name__)



DATABASE = []
for val in open('datapoints.txt').read().split("\n"):
	try:
		lat, lon = str(val).split(', ')
		DATABASE.append({"Longitude": lon, "Latitude": lat})
	except:
		pass


@app.route('/', methods=['GET'])
def index():
	return render_template("mainMap.html", DATABASE=DATABASE)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)