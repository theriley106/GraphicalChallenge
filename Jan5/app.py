import glob
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv

app = Flask(__name__)


usernames = []
DATABASE = []

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)


for val in your_list:
	usernames.append(val[1])

for user in list(set(usernames)):
	DATABASE.append({"User": user, "Count": usernames.count(user)})

DATABASE = sorted(DATABASE, key=lambda k: k['Count'], reverse=True)[:5]


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", DATABASE=DATABASE)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)