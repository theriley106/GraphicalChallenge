import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv
import sqlite3 as lite
import requests
app = Flask(__name__)
con = lite.connect('gasPrices.db')

cur = con.cursor()
cur.execute("DELETE FROM Information")
con.commit()

def retrieveDB():
	with con:
		cur = con.cursor()
		cur.execute("SELECT Price, StoreID, GasType FROM Information")
		return cur.fetchall()

def updateDB():
	info = []
	res = requests.get('http://zingon-data.com/spinx/prices.csv')
	decoded_content = res.content.decode('utf-8')
	cr = csv.reader(decoded_content.splitlines(), delimiter=',')
	my_list = list(cr)
	cur = con.cursor()
	for row in my_list:
		try:
			newVal = []
			for val in row:
				if len(val.strip()) > 2:
					newVal.append(val.strip())
			StoreID, Value, GasType, Price = tuple(newVal)
			cur.execute("INSERT INTO Information(StoreID) VALUES ({})".format(StoreID))
			cur.execute("Update Information SET Price=? WHERE StoreID=?", (Price, StoreID))
			cur.execute("Update Information SET GasType=? WHERE StoreID=?", (GasType, StoreID))
			cur.execute("Update Information SET GasType=? WHERE StoreID=?", (GasType, StoreID))
		except Exception as exp:
			print exp
	con.commit()






@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", belowAveragePrice=a, aboveAveragePrice=(len(Prices) - a))

if __name__ == "__main__":
	updateDB()
	Prices = []
	data = retrieveDB()
	for d in data:
		Prices.append(d[0])
	a = 0
	for d in Prices:
		if d < sum(tuple(Prices)) / len(Prices):
			a += 1
	print a

	app.run(host='0.0.0.0', port=8888)