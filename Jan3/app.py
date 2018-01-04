import csv
import datetime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify

import operator
app = Flask(__name__)

DATABASE = [0]

count = {}
for num in range(31):
	count['{0:02d}'.format(num+1)] = 0

#print count

def returnTime(timestamp):
	return (
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%d')
	)

def returnAllComments():
	with open('wsbcomments.csv', 'rb') as f:
		reader = csv.reader(f)
		for value in list(reader)[1:]:
			if 'tesla' in str(value[0]).lower() or 'tsla' in str(value[0]).lower() or '$tsla' in str(value[0]).lower():
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('$tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tesla')

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", DATABASE=DATABASE)

if __name__ == '__main__':
	returnAllComments()
	count = sorted(count.items(), key=operator.itemgetter(0))
	print count
	for key, value in count:
		DATABASE.append(value)
	app.run(host='127.0.0.1', port=8000)