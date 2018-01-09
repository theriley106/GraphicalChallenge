import glob
import csv
import sqlite3 as lite
import requests
con = lite.connect(glob.glob('static/Jan6.db')[0])


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

def getDatabase():
	updateDB()
	Prices = []
	data = retrieveDB()
	for d in data:
		Prices.append(d[0])
	a = 0
	for d in Prices:
		if d < sum(tuple(Prices)) / len(Prices):
			a += 1
	return (a, (len(Prices) - a))