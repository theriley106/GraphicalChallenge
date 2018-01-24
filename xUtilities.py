import random
import glob
import os
import string
import time
from selenium import webdriver
import bs4
import requests

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

def grabViewCount(redditURL):
	userName = os.environ['REDDIT_USERNAME']
	passWord = os.environ['REDDIT_PASSWORD']

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(redditURL, headers=headers)