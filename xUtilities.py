import re
import random
import glob
import os
import string
import time
from selenium import webdriver
import bs4
import requests
import threading
DB = {}

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

def grabViewCount(redditURL):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	a = redditLogin(headers)
	res = a.get(redditURL, headers=headers)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	e = page.select(".view-count")
	print(e[0].getText())
	return requests.get(redditURL, headers=headers)

#grabViewCount("https://www.reddit.com/r/wallstreetbets/comments/7pgyuj/pornhub_comments_containing_valid_stock_tickers/")
print extractRedditLinksFromFile()