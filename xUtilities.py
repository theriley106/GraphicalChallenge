import re
import threading
import random
import glob
import os
import string
import time
from selenium import webdriver
import bs4
import requests
import threading
try:
	from uszipcode import ZipcodeSearchEngine
	search = ZipcodeSearchEngine()
except:
	pass

def monthToMonth(shortMonth):
	try:
		return {
		'Jan' : "January",
		'Feb' : "February",
		'Mar' : "March",
		'Apr' : "April",
		'May' : "May",
		'Jun' : "June",
		'Jul' : "July",
		'Aug' : "August",
		'Sep' : "September",
		'Oct' : "October",
		'Nov' : "November",
		'Dec' : "December"
		}[shortMonth]
	except:
		return None

def returnLongLatFromCity(value):
	city, state = value.split(', ')
	a = search.by_city_and_state(city=city, state=state)[0]
	return a

def returnLongLatFromZIP(zipCode):
	a = search.by_zipcode(str(zipCode))[0]
	return {"Longitude": a["Longitude"], "Latitude": a["Latitude"]}

def chunks(l, n):
	"""Yield successive n-sized chunks from l."""
	for i in xrange(0, len(l), n):
		yield l[i:i + n]

def checkForScreenshot(date):
	fileName = "Screenshots/{}.png".format(date)
	return os.path.isfile(fileName)

def saveScreenshot(date):
	os.system("touch Screenshots/{}.png".format(date))
	driver = webdriver.Firefox()
	driver.get('http://127.0.0.1:5000/{}'.format(date))
	time.sleep(2)
	driver.save_screenshot('Screenshots/{}.png'.format(date))
	print("Saved")
	driver.close()

def genColor():
	r = lambda: random.randint(0,255)
	return str('#%02X%02X%02X' % (r(),r(),r()))

def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))

def redditLogin(headers):
	res = requests.session()
	data = [
	  ('op', 'login-main'),
	  ('user', os.environ['REDDIT_USERNAME']),
	  ('passwd', os.environ['REDDIT_PASSWORD']),
	  ('api_type', 'json'),
	]

	res.post('https://www.reddit.com/api/login/theriley106', headers=headers, data=data)
	return res

def extractRedditLinksFromFile(file="README.md"):
	links = []
	for link in re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', open(file).read()):
		if 'reddit' in str(link).lower():
			if ')' in str(link).lower():
				link = link[:-1]
			links.append(link)
	return links


def grabViewCount(redditURLList):
	info = []
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	listOfLinks = chunks(redditURLList, len(redditURLList) / 5)
	def extractView(redditURL):
		for url in redditURL:
			res = a.get(url, headers=headers)
			page = bs4.BeautifulSoup(res.text, 'lxml')
			e = page.select(".view-count")
			val = e[0].getText()
			if 'k' in str(val).lower():
				val = int(float(re.findall("([+-]?\d+\.\d+)", str(val))[0]) * 1000)
			info.append({"URL": url, "ViewCount": val})

	a = redditLogin(headers)
	threads = [threading.Thread(target=extractView, args=(url,)) for url in listOfLinks]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	return info

def genMakeIndex():
	DB = []
	for var in glob.glob('templates/*.html'):
		monthChoice = monthToMonth(re.findall('\D+', str(str(var).partition("/")[2]))[0])
		if monthChoice != None:
			DB.append({"Abbrev": re.findall('\D+', str(str(var).partition("/")[2]))[0], "Month": monthChoice, "Day": re.findall('\d+', str(str(var).partition("/")[2]))[0]})
		elif 'viz' in str(var):
			DB.append({"Abbrev": re.findall('\D+', str(str(var).partition("/")[2]))[0], "Month": "viz", "Day": re.findall('\d+', str(str(var).partition("/")[2]))[0]})
	DB.append({"Abbrev": "Mar", "Month": "Mar", "Day": "20"})
	DB.append({"Abbrev": "Mar", "Month": "Mar", "Day": "19"})
	return sorted(DB, key=lambda k: int(k['Day']))

if __name__ == '__main__':
	pass
