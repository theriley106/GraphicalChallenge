import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from textblob import TextBlob
import csv
from datetime import datetime
import operator
import glob
import json
DATES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

'''listDictionaries = []
#DATES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#YearlySentiment = [{'Y': 0.09034703986216593, 'X': '2015'}, {'Y': 0.0977252561320153, 'X': '2014'}, {'Y': 0.09023169494940395, 'X': '2017'}, {'Y': 0.08492654004088508, 'X': '2016'}, {'Y': 0.08780669719691525, 'X': '2011'}, {'Y': 0.18463455149501662, 'X': '2010'}, {'Y': 0.09018244279449084, 'X': '2013'}, {'Y': 0.06930046609477233, 'X': '2012'}]
VALUES = {}
listDictionariesWSB = []
WSBDict = {}
ALLDict = {}'''
#unsorted = [{'Y': 0.05802908427908424, 'X': '10-2012'}, {'Y': 0.09327487787205355, 'X': '06-2016'}, {'Y': 0.09794013925625829, 'X': '04-2016'}, {'Y': 0.07647510831258215, 'X': '06-2015'}, {'Y': 0.09783512975285362, 'X': '06-2014'}, {'Y': 0.08462575612005721, 'X': '06-2017'}, {'Y': 0.0679703774372021, 'X': '10-2011'}, {'Y': 0.1002007301692806, 'X': '06-2011'}, {'Y': 0.07642184053512567, 'X': '06-2013'}, {'Y': 0.04450645365762082, 'X': '06-2012'}, {'Y': 0.10488361748847148, 'X': '08-2013'}, {'Y': 0.08425522310741894, 'X': '04-2013'}, {'Y': 0.09020157790272731, 'X': '05-2012'}, {'Y': 0.08808575304295846, 'X': '05-2013'}, {'Y': 0.08763488874467996, 'X': '08-2017'}, {'Y': 0.08167938330740386, 'X': '08-2016'}, {'Y': 0.0881951030406961, 'X': '05-2016'}, {'Y': 0.08462423456252295, 'X': '08-2014'}, {'Y': 0.08574416055623599, 'X': '10-2014'}, {'Y': 0.07174919872595968, 'X': '08-2012'}, {'Y': 0.06640664029457133, 'X': '08-2011'}, {'Y': 0.10160778695751192, 'X': '05-2014'}, {'Y': 0.08729795858888638, 'X': '05-2015'}, {'Y': 0.08889666609302789, 'X': '08-2015'}, {'Y': 0.0864273281434055, 'X': '05-2017'}, {'Y': 0.08931935816711485, 'X': '09-2014'}, {'Y': 0.09306135999212754, 'X': '09-2015'}, {'Y': 0.0798710014925157, 'X': '09-2016'}, {'Y': 0.09494638999475243, 'X': '09-2017'}, {'Y': 0.2947089947089947, 'X': '09-2010'}, {'Y': 0.12068573938139154, 'X': '09-2011'}, {'Y': 0.04081191533562219, 'X': '09-2012'}, {'Y': 0.13293011140207842, 'X': '09-2013'}, {'Y': 0.21904761904761907, 'X': '02-2011'}, {'Y': 0.07821870676062204, 'X': '02-2013'}, {'Y': 0.060506002071746036, 'X': '02-2012'}, {'Y': 0.08867567331780765, 'X': '02-2015'}, {'Y': 0.09522087567412471, 'X': '02-2014'}, {'Y': 0.09723181458248283, 'X': '02-2017'}, {'Y': 0.06852894304179506, 'X': '02-2016'}, {'Y': 0.09102801658096839, 'X': '10-2017'}, {'Y': 0.1037375969781969, 'X': '01-2014'}, {'Y': 0.10341394369414302, 'X': '01-2015'}, {'Y': 0.09188300869011994, 'X': '01-2016'}, {'Y': 0.08124435255321169, 'X': '01-2017'}, {'Y': 0.03964285714285713, 'X': '01-2011'}, {'Y': 0.12148542566553314, 'X': '01-2012'}, {'Y': 0.08239256176243605, 'X': '01-2013'}, {'Y': 0.027812590187590188, 'X': '11-2011'}, {'Y': 0.13333333333333333, 'X': '11-2010'}, {'Y': 0.08431432906931999, 'X': '11-2013'}, {'Y': 0.08770919631431762, 'X': '11-2012'}, {'Y': 0.09063110231900116, 'X': '11-2015'}, {'Y': 0.09897966638618748, 'X': '11-2014'}, {'Y': 0.08965902570292524, 'X': '11-2017'}, {'Y': 0.057938035457090226, 'X': '11-2016'}, {'Y': 0.09021775128332504, 'X': '05-2011'}, {'Y': 0.09015888376371711, 'X': '12-2014'}, {'Y': 0.08298471815714396, 'X': '12-2015'}, {'Y': 0.10993569921951175, 'X': '12-2016'}, {'Y': 0.15845238095238096, 'X': '12-2010'}, {'Y': 0.08942564169836893, 'X': '12-2011'}, {'Y': 0.08613336287581785, 'X': '12-2012'}, {'Y': 0.09495735120043654, 'X': '12-2013'}, {'Y': 0.12094099994042658, 'X': '03-2012'}, {'Y': 0.06844362869814934, 'X': '03-2013'}, {'Y': 0.09290352504638218, 'X': '03-2011'}, {'Y': 0.07909272748169123, 'X': '03-2016'}, {'Y': 0.10177330435188844, 'X': '03-2017'}, {'Y': 0.09642324091090557, 'X': '03-2014'}, {'Y': 0.10839713905962088, 'X': '03-2015'}, {'Y': 0.09632401805807668, 'X': '04-2017'}, {'Y': 0.08217591220767875, 'X': '10-2013'}, {'Y': 0.08058401489661167, 'X': '04-2015'}, {'Y': 0.09513064939748919, 'X': '04-2014'}, {'Y': 0.09139789693223623, 'X': '10-2016'}, {'Y': 0.0781644430373684, 'X': '04-2012'}, {'Y': 0.25952380952380955, 'X': '04-2011'}, {'Y': 0.08978808760313482, 'X': '10-2015'}, {'Y': 0.07981941722524102, 'X': '07-2016'}, {'Y': 0.08521118879656597, 'X': '07-2017'}, {'Y': 0.11609089192525911, 'X': '07-2014'}, {'Y': 0.08035191286239954, 'X': '07-2015'}, {'Y': 0.04665426405312624, 'X': '07-2012'}, {'Y': 0.10513996154959347, 'X': '07-2013'}, {'Y': 0.0, 'X': '07-2010'}, {'Y': 0.0961149755127028, 'X': '07-2011'}] 
#newData = sorted(unsorted, key=lambda day: datetime.strptime(day['X'], "%m-%Y"))
#for val in newData:
#	val["X"] = "{}, {}".format(DATES[int(val['X'].partition("-")[0])-1], val['X'].partition('-')[2])
#print(len(newData))
def returnTime(timestamp):
	return (
	datetime.datetime.fromtimestamp(
		int(timestamp)
	).strftime('%m-%Y')
	)

'''
with open(glob.glob('static/Jan15/martinWSB.json')[0], 'rb') as f:
	for line in f:
		j_content = json.loads(line)
		testimonial = TextBlob(str(j_content['body']))
		day = returnTime(j_content['created_utc'])
		if day not in WSBDict:
			WSBDict[day] = []
		WSBDict[day].append(testimonial.sentiment.polarity)


with open(glob.glob('static/Jan15/martinAll.json')[0], 'rb') as f:
	for line in f:
		j_content = json.loads(line)
		day = returnTime(j_content['created_utc'])
		if day in WSBDict:
			testimonial = TextBlob(str(j_content['body']))
			if day not in ALLDict:
				ALLDict[day] = []
			ALLDict[day].append(testimonial.sentiment.polarity)
'''
#for e in range(7):
#	DATA.append({"Day": e, "Score": sum(DATABASE[e]) / float(len(DATABASE[e]))})

#print DATA
WSB = json.load(open(glob.glob('static/Jan15/WSB.json')[0], 'rb'))
ALL = json.load(open(glob.glob('static/Jan15/ALL.json')[0], 'rb'))


newDataWSB = sorted(WSB, key=lambda day: datetime.strptime(day['Day'], "%m-%Y"))
newDataALL = sorted(ALL, key=lambda day: datetime.strptime(day['Day'], "%m-%Y"))
for val in newDataWSB:
	val["Date"] = "{}, {}".format(DATES[int(val['Day'].partition("-")[0])-1], val['Day'].partition('-')[2])
for val in newDataALL:
	val["Date"] = "{}, {}".format(DATES[int(val['Day'].partition("-")[0])-1], val['Day'].partition('-')[2])

def getDatabase():
	DATABASE = {}
	DATABASE['WSB'] = newDataWSB
	DATABASE['ALL'] = newDataALL
	return DATABASE

'''WSB = []
ALL = []

for key, value in WSBDict.items():
	WSB.append({"Day": key, "Value": sum(value) / float(len(value))})
for key, value in ALLDict.items():
	ALL.append({"Day": key, "Value": sum(value) / float(len(value))})
with open('WSB.json', 'w') as fout:
	json.dump(WSB, fout)

with open('ALL.json', 'w') as fout:
	json.dump(ALL, fout)'''

if __name__ == '__main__':
	main()