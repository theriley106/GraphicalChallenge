import os
stocks = open("tickers.txt").read().split('\n')
for i, stock in enumerate(stocks):
	try:
		os.system("grep -rnw 'raw_data/' -e '{}' >> data.txt".format(stock.lower()))
		print("{} of {} completed".format(i, len(stocks)))
	except:
		print("Error")