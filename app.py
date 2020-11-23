try:
	# encoding=utf8
	import sys
	reload(sys)
	sys.setdefaultencoding('utf8')
except:
	pass

import os
import glob
import random
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv
import sqlite3 as lite
import requests
import threading
import json
import sys
import xUtilities
import readKaggle
import getInfo
from operator import itemgetter
import bs4
import re
import time
sys.path.insert(0, 'pythonFiles/')
app = Flask(__name__, static_url_path="", static_folder="static")

def gen_nested_lists(lists, n):
	a = []
	while len(lists) > 0:
		temp = []
		for i in range(min(len(lists),n)):
			x = lists.pop(0)
			x['hackathon'] = ""
			if ' at ' in x['title']:
				hackathon = x['title'].partition(" at ")[2]
				x['title'] = x['title'].partition(" at ")[0]
				x['hackathon'] = hackathon
			temp.append(x)
		a.append(temp)
	return a

@app.route('/callmemaybe', methods=["GET"])
def redirectToHerokuApp():
	return redirect("https://callmemaybeplatform.herokuapp.com/", code=302)

@app.route('/', methods=['GET'])
def index():
	infoVals = getInfo.all()
	dbVals = xUtilities.genMakeIndex()
	for i, val in enumerate(dbVals):
		keyVal = val['Abbrev'] + val["Day"]
		if keyVal not in infoVals:
			dbVals[i]['description'] = "No Info"
		else:
			dbVals[i]['description'] = infoVals[keyVal]
	newList = []
	for val in dbVals:
		if val['description'] != "No Info":
			newList.append(val)
	aboutMe = open("static/About.txt").read()
	return render_template("index.html", DATABASE=newList, KAGGLE_DATABASE=readKaggle.getAll(), ABOUTME=aboutMe)

@app.route('/uberAuthz', methods=['GET'])
def uberAuth():
	authCode = request.args.get("code")
	headers = {
	    'Authorization': 'Bearer {}'.format(authCode),
	    'Accept-Language': 'en_US',
	    'Content-Type': 'application/json',
	}
	response = requests.get('https://api.uber.com/v1.2/me', headers=headers)
	try:
		f = response.text
	except Exception as exp:
		f = '{"picture":"https:\/\/d1w2poirtb3as9.cloudfront.net\/4cda732c1c0b820c1a9a.jpeg?Expires=1551677991&Signature=XrOHk8RC2eW3eS-Oskt-tNIo1yN~tNlESgzO2Be6c2GP4eghwCWhcFkCvRgEoE-~Um71Dta1UAFnIftW0kY-WJxPtiyh5G6JA1~AI0U4f2r0jI-Iuq4SXKKU7H2cV39VnrSXxEaeWuWaX~yXWsz9kwTra4dzL6Qli8KSnIfhPJNjw5xSLiTYtSLjDicLtqNJUrrO3GzjeABr2A4TEoNJmlpXeWC2xfEZu39JPzHf1Mlf7Iz4w0fBdF48Pz77W5ERkfSR9J2ELvHMbSizUBFuBQ3sayB-iWGWdbOhMfjxblT6ZUuUa-M5kdAEn16vtcADnjwvWiHIU9Wzu1iXqhTEOw__&Key-Pair-Id=APKAJSDH2OZQQSA64LQQ","first_name":"Christopher","last_name":"Lambert","promo_code":"christopherl13389ue","rider_id":"8Kix-FUZD7CmSDTDAG-oreU2UX6msGna-jDIdbfy-P1r5ajFFK2-tS-4zrSOZNwAEy4Z7T0PX0i5ogt9862m0cdpPZlfqZIs7bNMCN4MQt5449XcCWGOD0G6licXw9IrhA==","email":"christopherlambert106@gmail.com","mobile_verified":true,"uuid":"4783d670-53d1-4b55-9a58-b5d3eaca6edb"}'
	if 'unauthorized' in str(f):
		f = '{"picture":"https:\/\/d1w2poirtb3as9.cloudfront.net\/4cda732c1c0b820c1a9a.jpeg?Expires=1551677991&Signature=XrOHk8RC2eW3eS-Oskt-tNIo1yN~tNlESgzO2Be6c2GP4eghwCWhcFkCvRgEoE-~Um71Dta1UAFnIftW0kY-WJxPtiyh5G6JA1~AI0U4f2r0jI-Iuq4SXKKU7H2cV39VnrSXxEaeWuWaX~yXWsz9kwTra4dzL6Qli8KSnIfhPJNjw5xSLiTYtSLjDicLtqNJUrrO3GzjeABr2A4TEoNJmlpXeWC2xfEZu39JPzHf1Mlf7Iz4w0fBdF48Pz77W5ERkfSR9J2ELvHMbSizUBFuBQ3sayB-iWGWdbOhMfjxblT6ZUuUa-M5kdAEn16vtcADnjwvWiHIU9Wzu1iXqhTEOw__&Key-Pair-Id=APKAJSDH2OZQQSA64LQQ","first_name":"Christopher","last_name":"Lambert","promo_code":"christopherl13389ue","rider_id":"8Kix-FUZD7CmSDTDAG-oreU2UX6msGna-jDIdbfy-P1r5ajFFK2-tS-4zrSOZNwAEy4Z7T0PX0i5ogt9862m0cdpPZlfqZIs7bNMCN4MQt5449XcCWGOD0G6licXw9IrhA==","email":"christopherlambert106@gmail.com","mobile_verified":true,"uuid":"4783d670-53d1-4b55-9a58-b5d3eaca6edb"}'
	return render_template("buttonUber.html", RESPONSE=f)


@app.route('/dataVisualizations', methods=['GET'])
def dataVizPage():
	infoVals = getInfo.all()
	dbVals = xUtilities.genMakeIndex()

	y = json.loads(open("links.json").read())
	for i, val in enumerate(dbVals):
		keyVal = val['Abbrev'] + val["Day"]
		if keyVal not in infoVals:
			dbVals[i]['description'] = "No Info"
		else:
			dbVals[i]['description'] = infoVals[keyVal]
			if keyVal in y:
				dbVals[i]['liveSite'] = y[keyVal]
	newList = []
	for val in dbVals:
		if val['description'] != "No Info":
			newList.append(val)

	return render_template("dataViz.html", DATABASE=newList, KAGGLE_DATABASE=readKaggle.getAll())

@app.route('/datasets', methods=['GET'])
def datasets():
	infoVals = getInfo.all()
	dbVals = xUtilities.genMakeIndex()

	for i, val in enumerate(dbVals):
		keyVal = val['Abbrev'] + val["Day"]
		if keyVal not in infoVals:
			dbVals[i]['description'] = "No Info"
		else:
			dbVals[i]['description'] = infoVals[keyVal]
	newList = []
	for val in dbVals:
		if val['description'] != "No Info":
			newList.append(val)
	return render_template("datasets.html", DATABASE=newList, KAGGLE_DATABASE=readKaggle.getAll())

@app.route('/personalProjects', methods=['GET'])
def personalProjects():
	infoVals = getInfo.all()
	dbVals = xUtilities.genMakeIndex()
	for i, val in enumerate(dbVals):
		keyVal = val['Abbrev'] + val["Day"]
		if keyVal not in infoVals:
			dbVals[i]['description'] = "No Info"
		else:
			dbVals[i]['description'] = infoVals[keyVal]
	newList = []
	for val in dbVals:
		if val['description'] != "No Info":
			newList.append(val)
	personalProjectDB = json.loads(open("static/personalProjects.json").read())
	for val in personalProjectDB:
		val['liveSite'] = (len(val.get('liveSiteURL', "")) > 1)
	ppDB = []
	while len(personalProjectDB) > 0:
		a = []
		for i in range(3):
			if len(personalProjectDB) == 0:
				break
			a.append(personalProjectDB.pop(0))
		ppDB.append(a)
	return render_template("personalProjects.html", DATABASE=newList, PERSONAL_PROJECTS=ppDB)

@app.route('/other', methods=['GET'])
def other():
	infoVals = getInfo.all()
	dbVals = xUtilities.genMakeIndex()
	for i, val in enumerate(dbVals):
		keyVal = val['Abbrev'] + val["Day"]
		if keyVal not in infoVals:
			dbVals[i]['description'] = "No Info"
		else:
			dbVals[i]['description'] = infoVals[keyVal]
	newList = []
	for val in dbVals:
		if val['description'] != "No Info":
			newList.append(val)
	other = json.loads(open("static/other.json").read())
	other = gen_nested_lists(other, 3)
	return render_template("other.html", DATABASE=newList, OTHER=other)

@app.route('/random', methods=['GET'])
def randomStuff():
	linkVals = open("static/randomLinks.txt").read().split("\n")
	return render_template("randomLinks.html", links=linkVals)

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

@app.route('/Jan4/', methods=['GET'])
def Jan4():
	import Jan4
	return render_template("Jan4.html", DATABASE=Jan4.getDatabase())
#This is template for all sites

@app.route('/Jan5/', methods=['GET'])
def Jan5():
	import Jan5
	return render_template("Jan5.html", DATABASE=Jan5.getDatabase())
#This is template for all sites

@app.route('/Jan6/', methods=['GET'])
def Jan6():
	import Jan6
	belowAveragePrice, aboveAveragePrice = Jan6.getDatabase()
	return render_template("Jan6.html", belowAveragePrice=belowAveragePrice, aboveAveragePrice=aboveAveragePrice)
#This is template for all sites

@app.route('/Jan7/', methods=['GET'])
def Jan7():
	return render_template("Jan7.html")
#This is template for all sites

@app.route('/Jan8/', methods=['GET'])
def Jan8():
	import Jan8
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan8.html", DATABASE=Jan8.getDatabase())
#This is template for all sites

@app.route('/Jan9/', methods=['GET'])
def Jan9():
	import Jan9
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	DATABASE = Jan9.getDatabase()
	return render_template("Jan9.html", DATABASE=DATABASE, DATA=range(1,len(DATABASE) / 4))
#This is template for all sites

@app.route('/Jan10/', methods=['GET'])
def Jan10():
	import Jan10
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan10.html", DATABASE=Jan10.getDatabase())
#This is template for all sites

@app.route('/Jan11/', methods=['GET'])
def Jan11():
	import Jan11
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan11.html", DATABASE=Jan11.getDatabase())
#This is template for all sites

@app.route('/Jan12/', methods=['GET'])
def Jan12():
	import Jan12
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan12.html", DATABASE=Jan12.getDatabase())
#This is template for all sites

@app.route('/Jan13/', methods=['GET'])
def Jan13():
	import Jan13
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan13.html", DATABASE=Jan13.getDatabase())
#This is template for all sites

@app.route('/Jan14/', methods=['GET'])
def Jan14():
	import Jan14
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan14.html", DATABASE=Jan14.getDatabase())
#This is template for all sites

@app.route('/Jan15/', methods=['GET'])
def Jan15():
	import Jan15
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	#if
	DATABASE = Jan15.getDatabase()
	return render_template("Jan15.html", WSB=DATABASE['WSB'], ALL=DATABASE['ALL'])
#This is template for all sites

@app.route('/Jan16/', methods=['GET'])
def Jan16():
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan16.html")

@app.route('/Jan17/', methods=['GET'])
def Jan17():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	DATABASE = sorted(DATABASE, key=lambda k: k['Nootropics']['Occurances'])
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan17.html", DATABASE=DATABASE[::-1][:15])

@app.route('/Jan18/', methods=['GET'])
def Jan18():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	DATABASE = sorted(DATABASE, key=lambda k: k['Nootropics']['Occurances'])
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan18.html", DATABASE=DATABASE[::-1][:10])

@app.route('/Jan19/', methods=['GET'])
def Jan19():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	DATABASE = sorted(DATABASE, key=lambda k: k['StackAdvice']['Occurances'])
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan19.html", DATABASE=DATABASE[::-1][:10])

@app.route('/Jan20/', methods=['GET'])
def Jan20():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	for data in DATABASE:
		data['TotalOccurances'] = data['StackAdvice']['Occurances'] + data['Nootropics']['Occurances']
		data['ColorVal'] = {"Name": xUtilities.random_char(5), "Color": xUtilities.genColor()}
	DATABASE = sorted(DATABASE, key=lambda k: k['TotalOccurances'])
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan20.html", DATABASE=DATABASE[::-1][:30])

@app.route('/Jan21/', methods=['GET'])
def Jan21():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	for data in DATABASE:
		data['TotalOccurances'] = data['StackAdvice']['Occurances'] + data['Nootropics']['Occurances']
		data['ColorVal'] = {"Name": xUtilities.random_char(5), "Color": xUtilities.genColor()}
	for data in DATABASE:
		data['totalSentiment'] = float(data['Nootropics']['Sentiment'] + data['StackAdvice']['Sentiment']) / 2
		#data['totalSentiment'] = ((data['Nootropics']['Sentiment'] * data['Nootropics']['Occurances']) + (data['StackAdvice']['Sentiment'] * data['StackAdvice']['Occurances'])) / data['TotalOccurances']
	for data in DATABASE:
		print(data['totalSentiment'])
		data['Nootropics']['Sentiment'] = round(data['Nootropics']['Sentiment'], 4)
		data['StackAdvice']['Sentiment'] = round(data['StackAdvice']['Sentiment'], 4)
	DATABASE = sorted(DATABASE, key=lambda k: k['totalSentiment'])
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan21.html", DATABASE=DATABASE[::-1])

@app.route('/Jan22/', methods=['GET'])
def Jan22():
	import Jan22
	DATABASE=Jan22.getDatabase()
	DATABASE = sorted(DATABASE, key=lambda k: k['Score'])
	date = sys._getframe().f_code.co_name
	#print (float(listOf99) / float(2143)) * 100
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan22.html", DATABASE=DATABASE[10:])

@app.route('/Jan23/', methods=['GET'])
def Jan23():
	import Jan23
	DATABASE=Jan23.getDatabase()
	DATABASE = sorted(DATABASE, key=lambda k: int(k['Score']))
	date = sys._getframe().f_code.co_name
	#print (float(listOf99) / float(2143)) * 100
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan23.html", DATABASE=DATABASE[10:])

@app.route('/Jan24/', methods=['GET'])
def Jan24():
	import Jan24
	date = sys._getframe().f_code.co_name
	#print (float(listOf99) / float(2143)) * 100
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	DATABASE=Jan24.getDatabase()
	return render_template("Jan24.html", DATABASE=DATABASE)

@app.route('/Jan25/', methods=['GET'])
def Jan25():
	import Jan24
	DATABASE=Jan24.getDatabase()
	#import Jan25
	#DATABASE=Jan25.getDatabase()
	return render_template("Jan25.html", DATABASE=DATABASE)

@app.route('/Jan26/', methods=['GET'])
def Jan26():
	return render_template("Jan26.html")

@app.route('/Jan27/', methods=['GET'])
def Jan27():
	import Jan27
	DATABASE=Jan27.getDatabase()
	#import Jan25
	#DATABASE=Jan25.getDatabase()
	return render_template("Jan27.html", DATABASE=DATABASE)

@app.route('/Jan29/', methods=['GET'])
def Jan29():
	import Jan29
	date = sys._getframe().f_code.co_name
	#print (float(listOf99) / float(2143)) * 100
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	DATABASE=Jan29.getDatabase()
	return render_template("Jan29.html", DATABASE=DATABASE)


@app.route('/Jan31/', methods=['GET'])
def Jan31():
	import Jan31
	DATABASE=Jan31.getDatabase()
	#import Jan25
	#DATABASE=Jan25.getDatabase()
	return render_template("Jan31.html", DATABASE=DATABASE)

@app.route('/Feb1/', methods=['GET'])
def Feb1():
	import Feb1
	DATABASE=Feb1.getDatabase()

	return render_template("Feb1.html", DATABASE=DATABASE)

@app.route('/Feb2/', methods=['GET'])
def Feb2():
	import Feb2
	date = sys._getframe().f_code.co_name
	#print (float(listOf99) / float(2143)) * 100
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	DATABASE=Feb2.getDatabase()[:-1]

	return render_template("Feb2.html", DATABASE=DATABASE)

@app.route('/Feb3/', methods=['GET'])
def Feb3():
	DATABASE = []
	try:
		DATABASE = Feb3.getDatabase()
	except:
		import Feb3
		DATABASE = Feb3.getDatabase()
	date = sys._getframe().f_code.co_name
	#print (float(listOf99) / float(2143)) * 100
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan29.html", DATABASE=DATABASE)

@app.route('/Feb4/', methods=['GET'])
def Feb4():
	import Feb4
	DATABASE = Feb4.getDatabase()
	return render_template("Feb4.html", DATABASE=DATABASE)


@app.route('/Mar16/', methods=['GET'])
def Mar16():
	import Mar16
	DATABASE = Mar16.getDatabase()
	return render_template("Mar16.html", DATABASE=DATABASE)

@app.route('/Mar17/', methods=['GET'])
def Mar17():
	import Mar17
	DATABASE = Mar17.getDatabase()
	return render_template("Mar17.html", DATABASE=DATABASE)

@app.route('/Mar18/', methods=['GET'])
def Mar18():
	import Mar18
	DATABASE = Mar18.getDatabase()
	return render_template("Mar18.html", DATABASE=DATABASE)

@app.route('/Mar19/', methods=['GET'])
def Mar19():
	import Mar19
	# Generates the overall analysis from /all
	MHH = []
	# Mean household income
	dataset = Mar19.ResponseByZipAsLod()
	# Returns the response time from each zip as a list of dictionaries
	zipVal = Mar19.returnHousholdIncome()
	# Returns the household incomes for each zip as a python dict
	for zipC in Mar19.getZipCodes():
		# Iterates through all zip codes in the dataset
		MHH.append({"Zip": zipC, "MHH": int(zipVal[zipC]["Income"].replace(",", ""))})
		# Appends the values to the mean household income dataset
	MHH = sorted(MHH, key=itemgetter('MHH'), reverse=False)
	# Sorts the values
	distanceFrom = json.load(open("static/distance_from.json"))
	# Loads the distance dataset
	distanceFrom = sorted(distanceFrom, key=itemgetter('Distance'), reverse=False)
	return render_template("zipResponseViz.html", responseTimeData=dataset, MeanIncome=MHH, DistanceFrom=distanceFrom)

@app.route('/Mar20/', methods=['GET'])
def Mar20():
	import Mar19
	# Generates the overall analysis from /all
	MHH = []
	# Mean household income
	dataset = Mar19.ResponseByZipAsLod()
	# Returns the response time from each zip as a list of dictionaries
	zipVal = Mar19.returnHousholdIncome()
	# Returns the household incomes for each zip as a python dict
	for zipC in Mar19.getZipCodes():
		# Iterates through all zip codes in the dataset
		MHH.append({"Zip": zipC, "MHH": int(zipVal[zipC]["Income"].replace(",", ""))})
		# Appends the values to the mean household income dataset
	MHH = sorted(MHH, key=itemgetter('MHH'), reverse=False)
	# Sorts the values
	distanceFrom = json.load(open("static/distance_from.json"))
	# Loads the distance dataset
	distanceFrom = sorted(distanceFrom, key=itemgetter('Distance'), reverse=False)
	return render_template("distanceFrom.html", responseTimeData=dataset, MeanIncome=MHH, DistanceFrom=distanceFrom)

@app.route('/Mar21/', methods=['GET'])
def Mar21():
	import Mar19
	# Generates the overall analysis from /all
	MHH = []
	# Mean household income
	dataset = Mar19.ResponseByZipAsLod()
	# Returns the response time from each zip as a list of dictionaries
	zipVal = Mar19.returnHousholdIncome()
	# Returns the household incomes for each zip as a python dict
	for zipC in Mar19.getZipCodes():
		# Iterates through all zip codes in the dataset
		MHH.append({"Zip": zipC, "MHH": int(zipVal[zipC]["Income"].replace(",", ""))})
		# Appends the values to the mean household income dataset
	MHH = sorted(MHH, key=itemgetter('MHH'), reverse=False)
	# Sorts the values
	distanceFrom = json.load(open("static/distance_from.json"))
	# Loads the distance dataset
	distanceFrom = sorted(distanceFrom, key=itemgetter('Distance'), reverse=False)
	return render_template("meanIncome.html", responseTimeData=dataset, MeanIncome=MHH, DistanceFrom=distanceFrom)

@app.route('/Mar22/', methods=['GET'])
def Mar22():
	import Mar19
	# Generates the overall analysis from /all
	MHH = []
	# Mean household income
	dataset = Mar19.ResponseByZipAsLod()
	# Returns the response time from each zip as a list of dictionaries
	zipVal = Mar19.returnHousholdIncome()
	# Returns the household incomes for each zip as a python dict
	for zipC in Mar19.getZipCodes():
		# Iterates through all zip codes in the dataset
		MHH.append({"Zip": zipC, "MHH": int(zipVal[zipC]["Income"].replace(",", ""))})
		# Appends the values to the mean household income dataset
	MHH = sorted(MHH, key=itemgetter('MHH'), reverse=False)
	# Sorts the values
	distanceFrom = json.load(open("static/distance_from.json"))
	# Loads the distance dataset
	distanceFrom = sorted(distanceFrom, key=itemgetter('Distance'), reverse=False)
	return render_template("pieChart.html", responseTimeData=dataset, MeanIncome=MHH, DistanceFrom=distanceFrom)

@app.route('/viz43', methods=['GET'])
def viz43():
	import viz43
	return render_template("viz43.html", DATABASE=viz43.getDatabase())

@app.route('/viz44', methods=['GET'])
def viz44():
	import viz44
	return render_template("viz44.html", DATABASE=viz44.getDatabase())


@app.route('/viz45', methods=['GET'])
def viz45():
	import viz45
	DATABASE = viz45.getDatabase()
	DATABASE = sorted(DATABASE, key=lambda k: k['Age'])
	return render_template("viz45.html", DATABASE=DATABASE)

@app.route('/viz46', methods=['GET'])
def viz46():
	import viz46
	DATABASE = viz46.getDatabase()
	return render_template("viz46.html", DATABASE=DATABASE)

@app.route('/viz47/', methods=['GET'])
def viz47():
	import viz47
	DATABASE=viz47.getDatabase()
	return render_template("viz47.html", DATABASE=DATABASE)

@app.route('/viz48/', methods=['GET'])
def viz48():
	import viz48
	DATABASE=viz48.getDatabase()
	return render_template("viz48.html", DATABASE=DATABASE)

@app.route('/viz49/', methods=['GET'])
def viz49():
	import viz49
	DATABASE=viz49.getDatabase()
	return render_template("viz49.html", DATABASE=DATABASE)

@app.route('/viz50/', methods=['GET'])
def viz50():
	import viz50
	DATABASE=viz50.getDatabase()
	return render_template("viz50.html", DATABASE=DATABASE)

@app.route('/viz51', methods=['GET'])
def viz51():
	import viz51
	DATABASE=viz51.getDatabase()
	return render_template("viz51.html", DATABASE=DATABASE)

@app.route('/viz52', methods=['GET'])
def viz52():
	import viz52
	DATABASE=viz52.getDatabase()
	return render_template("viz52.html", DATABASE=DATABASE)

@app.route('/walmartSKUs', methods=['GET'])
def walmartSKUs():
	return send_file("static/skus.txt", as_attachment=True)

@app.route('/company', methods=['GET'])
def company():
	return render_template("ourCompany.html")

@app.route('/duolingo', methods=['GET'])
def duolingo():
	result = requests.get("https://www.duolingo.com/2017-06-30/users?username=theriley106&_={}".format(int(time.time()))).json()
	return jsonify({"streak": result['users'][0]['streak']})

@app.route('/streaks', methods=['GET'])
def streaks():
	return render_template("streaks.html")

@app.route('/leetcode', methods=['GET'])
def getLeetcode():
	try:
		res = requests.get("https://leetcode.com/theriley106/")
		page = bs4.BeautifulSoup(res.text, 'lxml')
		num = "INVALID"
		for val in page.select(".list-group-item"):
			if 'solved question' in str(val.getText()).lower():
				print(val.getText())
				num = int(re.findall("\d+", str(val.getText()).lower())[0])
	except Exception as exp:
		num = 0
	return jsonify({"value": num})

@app.route('/columbiaOnline', methods=['GET'])
def columbiaOnline():
	return render_template("columbiaOnline.html")

if __name__ == "__main__":
	app.run(debug=True)




