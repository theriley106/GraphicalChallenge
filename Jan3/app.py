import csv
import datetime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import finance
import operator
app = Flask(__name__)

DATABASE = [0]




#print count

def returnTime(timestamp):
	return (
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%d')
	)

def returnAllComments(stock):
	count = {}
	for num in range(31):
		count['{0:02d}'.format(num+1)] = 0
	with open('wsbcomments.csv', 'rb') as f:
		reader = csv.reader(f)
		for value in list(reader)[1:]:
			'''
			if 'tesla' in str(value[0]).lower() or 'tsla' in str(value[0]).lower() or '$tsla' in str(value[0]).lower():
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('$tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tesla')'''
			if '${}'.format(stock.lower()) in str(value[0]).lower() or '{}'.format(stock.lower()) in str(value[0]).lower():
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('${}'.format(stock))
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('{}'.format(stock))
	return count
@app.route('/<stock>', methods=['GET'])
def index(stock):
	count = returnAllComments(stock)
	count = sorted(count.items(), key=operator.itemgetter(0))
	print count
	for key, value in count:
		DATABASE.append(value)
	allDays = []
	allValues = []
	stockData = finance.get_historical_data(stock)
	#for key, value in DATABASE:

	#for key, value in stockData.items():
	for key, value in stockData.items():
		allDays.append(key)
	for value in allDays:
		for key, valuez in count:
			if key == value:
				diff = stockData[value]
				allValues.append({"Day": value, "Difference": diff, "Comments": valuez})
	
	allValues = newlist = sorted(allValues, key=lambda k: k['Day'])
	return render_template("index.html", DATABASE=allValues)

if __name__ == '__main__':
	
	app.run(host='127.0.0.1', port=8000)