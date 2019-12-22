import os
from selenium import webdriver
import time

def save_ss(driver, fileName):
	element = driver.find_element_by_tag_name('body')
	element_png = element.screenshot_as_png
	with open(fileName, "wb") as file:
		file.write(element_png)

if __name__ == '__main__':
	currentDir = os.getcwd()
	a = os.getcwd() + "/app.py"
	a = "cd {} && python ".format(currentDir) + a
	a = '"{}"'.format(a)
	terminal = '"Terminal"'
	# a = "{}".format(currentDir, a)
	newCommand = "osascript -e 'tell application {} to do script {}'".format(terminal, a)
	print newCommand
	# newCommand = "cd {}".format(currentDir)
	os.system(newCommand)
	# print(a)
	driver = webdriver.Firefox()
	driver.get("http://127.0.0.1:5000")
	time.sleep(3)
	save_ss(driver, 'static/home.png')
	driver.get("http://127.0.0.1:5000/personalProjects")
	save_ss(driver, 'static/personalProjects.png')
	driver.get("http://127.0.0.1:5000/other")
	save_ss(driver, 'static/other.png')
	driver.get("http://127.0.0.1:5000/dataVisualizations")
	save_ss(driver, 'static/dataVisualizations.png')
	driver.quit()