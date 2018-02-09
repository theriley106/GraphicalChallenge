import requests
import bs4
import re
import json
from textblob import TextBlob

def getLyricSentiment(lyrics):
	lyrics = re.sub('\s+',' ',lyrics)
	return TextBlob(lyrics).sentiment.polarity

def grabSite(url):
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
	return requests.get(url, headers=headers)

def genSongUrl(songTitle, baseUrl='https://www.azlyrics.com/lyrics/panicatthedisco/{0}.html'):
	string = ''.join(re.findall('\w+', str(songTitle))).lower()
	if len(string) > 2:
		return baseUrl.format(string)
	else:
		return None

def grabLyrics(url):
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	lyrics = "<div>{}</div>".format(str(page).partition("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->")[2].partition("</div")[0])
	# I know this is an awful way of doing this ^
	page = bs4.BeautifulSoup(str(lyrics), 'lxml')
	return str(page.getText())


def grabAllSongs(url):
	listOfSongs = []
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	for i, songTitle in enumerate(page.select("#listAlbum a")):
		try:
			title = songTitle.getText()
			url = genSongUrl(title)
			if url != None:
				lyrics = grabLyrics(url)
				listOfSongs.append({"Title": title, "URL": url, "Lyrics": lyrics, "Sentiment": getLyricSentiment(lyrics)})
		except:
			print("Error on {}".format(i))
		print("Done with {}".format(i))
	return listOfSongs

if __name__ == '__main__':
	e = grabAllSongs("https://www.azlyrics.com/p/panicatthedisco.html")
	with open('data.json', 'w') as outfile:
		json.dump(e, outfile)
