import urllib2
from BeautifulSoup import BeautifulSoup as bs
import csv
import datetime
import operator
import glob
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
	with open(glob.glob('static/Jan3.csv')[0], 'rb') as f:
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

def get_historical_data(name):
	data = {}
	url = "https://finance.yahoo.com/quote/" + name + "/history/?period1=1512104400&period2=1514696400&interval=1d&filter=history&frequency=1d"
	rows = bs(urllib2.urlopen(url).read()).findAll('table')[0].tbody.findAll('tr')

	for each_row in rows:
		divs = each_row.findAll('td')
		if divs[1].span.text  != 'Dividend': #Ignore this row in the table
			#I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
			dateValue = ('{0:02d}'.format(int(str(divs[0].span.text).partition(' ')[2].partition(",")[0])))
			diff = (round(float(divs[1].span.text.replace(',','')) - float(divs[4].span.text.replace(',','')), 2))
			data[dateValue] = diff

	return data

def returnData(stock):
	DATABASE = [0]
	count = returnAllComments(stock)
	count = sorted(count.items(), key=operator.itemgetter(0))
	#print count
	for key, value in count:
		DATABASE.append(value)
	allDays = []
	allValues = []
	stockData = get_historical_data(stock)
	#for key, value in DATABASE:

	#for key, value in stockData.items():
	for key, value in stockData.items():
		allDays.append(key)
	for value in allDays:
		for key, valuez in count:
			if key == value:
				diff = stockData[value]
				allValues.append({"Day": value, "Difference": diff, "Comments": valuez})
	
	return sorted(allValues, key=lambda k: k['Day'])