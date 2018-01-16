import glob
import os

def checkForScreenshot(fileName):
	return os.path.isfile(fileName)

def saveScreenshot(url):
	driver = webdriver.PhantomJS()
	driver.get(url)
	driver.save_screenshot('static/{}.png'.format(proxy.partition(':')[0]))
	driver.quit()