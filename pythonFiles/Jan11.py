import requests
import bs4
import glob
import csv


COUNTRY_DB = {'Canada': [61.0666922, -107.9917071], 'Brazil': [-10.3333333, -53.2], 'Bangladesh': [24.4768783, 90.2932426], 'USA': [39.7837304, -100.4458825], 'Nepal': [28.1083929, 84.0917139], 'Cambodia': [13.5066394, 104.869423], 'Nigeria': [9.6000359, 7.9999721], 'Ghana': [8.0300284, -1.0800271], 'Australia': [-24.7761086, 134.755], 'Singapore': [1.357107, 103.8194992], 'China': [35.000074, 104.999927], 'Thailand': [14.8971921, 100.83273], 'Germany': [51.0834196, 10.4234469], 'Netherlands': [52.5001698, 5.7480821], 'Holland': [52.5001698, 5.7480821], 'Poland': [52.0977181, 19.0258159], 'Indonesia': [-4.7993356, 114.5632032], 'United States': [39.7837304, -100.4458825], 'UK': [54.7023545, -3.2765753], 'Sweden': [59.6749712, 14.5208584], 'Vietnam': [13.2904027, 108.4265113], 'Finland': [63.2467777, 25.9209164], 'Hungary': [47.1817585, 19.5060937], 'Taiwan': [23.9739374, 120.9820179], 'Pakistan': [30.3308401, 71.247499], 'Myanmar': [17.1750495, 95.9999652], 'Estonia': [58.7523778, 25.3319078], 'Mexico': [22.5000485, -100.0000375], 'India': [22.3511148, 78.6677428], 'Malaysia': [4.5693754, 102.2656823], 'Colombia': [2.8894434, -73.783892], 'Japan': [36.5748441, 139.2394179], 'South Korea': [36.5581914, 127.9408564], 'Fiji': [-18.1239696, 179.0122737]}
COUNTRIES = []
DATA = {'Canada': 2.24, 'Brazil': 4.35, 'Bangladesh': 3.71, 'USA': 3.46, 'Nepal': 3.55, 'Cambodia': 4.2, 'Nigeria': 1.5, 'Ghana': 3.5, 'Sarawak': 4.33, 'Australia': 3.14, 'Singapore': 4.13, 'China': 3.42, 'Thailand': 3.38, 'Germany': 3.64, 'Hong Kong': 3.8, 'Philippines': 3.33, 'Dubai': 3.58, 'Netherlands': 2.48, 'Holland': 3.56, 'Poland': 3.63, 'Indonesia': 4.07, 'United States': 3.75, 'UK': 3.0, 'Sweden': 3.25, 'Vietnam': 3.19, 'Finland': 3.58, 'Hungary': 3.61, 'Taiwan': 3.67, 'Pakistan': 3.0, 'Myanmar': 3.95, 'Estonia': 3.5, 'Mexico': 3.73, 'India': 3.4, 'Malaysia': 3.98, 'Colombia': 3.29, 'Japan': 3.98, 'South Korea': 3.79, 'Fiji': 3.88}

def get_boundingbox_country(country, output_as='center'):
    """
    get the bounding box of a country in EPSG4326 given a country name

    Parameters
    ----------
    country : str
        name of the country in english and lowercase
    output_as : 'str
        chose from 'boundingbox' or 'center'. 
         - 'boundingbox' for [latmin, latmax, lonmin, lonmax]
         - 'center' for [latcenter, loncenter]

    Returns
    -------
    output : list
        list with coordinates as str
    """
    # create url
    url = '{0}{1}{2}'.format('http://nominatim.openstreetmap.org/search?country=',
                             country,
                             '&format=json&polygon=0')
    response = requests.get(url).json()[0]

    # parse response to list
    if output_as == 'boundingbox':
        lst = response[output_as]
        output = [float(i) for i in lst]
    if output_as == 'center':
        lst = [response.get(key) for key in ['lat','lon']]
        output = [float(i) for i in lst]
    return output

def readCSVs():
    with open(glob.glob('static/Jan11.csv')[0], 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        for your_list in your_list:
            try:
                DATA[your_list[4]].append(float(your_list[5]))
            except:
                try:
                    DATA[your_list[4]] = []
                    DATA[your_list[4]].append(float(your_list[5]))
                except:
                    pass

readCSVs()
'''for country in list(set(COUNTRIES)):
    try:
        COUNTRY_DB[country] = get_boundingbox_country(country)
    except:
        print('error')'''
A = []

for key, value in DATA.items():
    if key != "Nigeria":
        try:
            A.append({"Value": round(sum(value)/len(value), 2), "Country": key})
        except:
            pass
def getDatabase():
    return sorted(A, key=lambda k: k['Value'])