import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv
import sqlite3 as lite
import requests
import sys
sys.path.insert(0, 'pythonFiles/')
app = Flask(__name__)

@app.route('/Jan1/', methods=['GET'])
def Jan1():
	import Jan1
	return render_template("Jan1.html", DATABASE=Jan1.genDatabase(), BUSNUM="4012715")
#This is template for all sites

@app.route('/Jan2/', methods=['GET'])
def Jan2():
	import Jan2
	return render_template("Jan2.html", DATABASE=Jan2.returnDatabase())
#This is template for all sites
@app.route('/Jan3', methods=['GET'])
@app.route('/Jan3/<stock>', methods=['GET'])
def Jan3(stock="TSLA"):
	import Jan3
	return render_template("Jan3.html", DATABASE=Jan3.returnData(stock))
#This is template for all sites

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)