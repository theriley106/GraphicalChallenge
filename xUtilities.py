import random
import glob
import os
import string
import time
from selenium import webdriver
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