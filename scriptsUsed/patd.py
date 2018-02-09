import requests
import bs4
import re


def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def genSongUrl(songTitle, baseUrl='https://www.azlyrics.com/lyrics/panicatthedisco/{0}.html'):
	string = ''.join(re.findall('\w+', str(songTitle))).lower()
	if len(string) > 2:
		return baseUrl.format(string)
	else:
		return None

def grabAllSongs(url):
	listOfSongs = []
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	for songTitle in page.select("#listAlbum a"):
		title = songTitle.getText()
		url = genSongUrl(title)
		if url != None:
			listOfSongs.append({"Title": title, "URL": url})
	return listOfSongs

if __name__ == '__main__':
	for var in grabAllSongs("https://www.azlyrics.com/p/panicatthedisco.html"):
		print var
	#res = grabSite()
	#page = bs4.BeautifulSoup(res.text, 'lxml')


