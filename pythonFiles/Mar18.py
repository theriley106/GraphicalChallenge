import glob
import json

DATA = []
info = json.load(open(glob.glob('static/ratingNum.json')[0], 'rb'))

for key, value in sorted(info.items(), key=lambda x:x[1], reverse=True)[:10]:
    DATA.append({"Value": float(value["Num"]) / float(value["Total"]), "School": key})

def getDatabase():
    return sorted(DATA, key=lambda k: k['Value'])
