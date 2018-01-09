import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import glob
import csv
import Image


def grabStar(string):
	try:
		if 'n/a' in str(string):
			return 0
		else:
			return int(str(string.replace(' ', '.')).partition('.')[0])
	except:
		print("Error")
		return 7

with open(glob.glob('../static/Jan7.csv')[0], 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

Data = []
for var in your_list:
	Data.append(str(grabStar(var[4])))
 
objects = ('n/a', '1 Star', '2 Star', '3 Star', '4 Star', '5 Star')
y_pos = np.arange(len(objects))
performance = [Data.count("0"),Data.count("1"),Data.count("2"),Data.count("3"),Data.count("4"),Data.count("5")]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Downloads')
plt.title('Alexa Skill Reviews')
 
plt.savefig('testplot.png')