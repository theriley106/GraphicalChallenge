import urllib2
from BeautifulSoup import BeautifulSoup as bs

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

#Test
if __name__ == '__main__':
	print get_historical_data('amzn')