import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv


app = Flask(__name__)


BUSNUM = "4012715"

def returnAllCSV(busNum):
	return glob.glob('static/Jan1.csv'.format(busNum))

def readCSVs():
	DATABASE = []
	for csvFile in returnAllCSV(BUSNUM):
		with open(csvFile, 'rb') as f:
			reader = csv.reader(f)
			your_list = list(reader)
			for your_listz in your_list:
				try:
					DATABASE.append({"Lat": your_listz[2], "Long": your_listz[1]})
				except Exception as exp:
					print exp
					pass
	return DATABASE

def genDatabase():
	DATABASE = readCSVs()
	DATABASE = [dict(t) for t in set([tuple(d.items()) for d in DATABASE])]
	DATABASE = DATABASE[:500]
	return DATABASE

