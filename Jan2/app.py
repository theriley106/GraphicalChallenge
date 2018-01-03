import csv
import datetime

DATABASE = []

count = {}
for num in range(31):
	count['{0:02d}'.format(num+1)] = 0

#print count

def returnTime(timestamp):
	return (
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%d')
	)

def returnAllComments():
	with open('wsbcomments.csv', 'rb') as f:
		reader = csv.reader(f)
		for value in list(reader)[1:]:
			if 'tesla' in str(value[0]).lower() or 'tsla' in str(value[0]).lower() or '$tsla' in str(value[0]).lower():
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('$tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tesla')

if __name__ == '__main__':
	returnAllComments()
	for key, value in count.items():
		print("{} - {}".format(key, value))
	