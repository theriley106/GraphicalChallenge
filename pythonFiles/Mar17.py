import glob
import json

DATA = []
info = json.load(open(glob.glob('static/howHot.json')[0], 'rb'))

for key, value in sorted(info.items(), key=lambda x:x[1])[:10]:
    DATA.append({"Value": value, "School": key})


def getDatabase():
    return sorted(DATA, key=lambda k: k['Value'])
