import glob
import os
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