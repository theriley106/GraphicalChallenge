import requests
import bs4
import time
import re
import tweepy
maleTweets = []
femaleTweets = []

# Consumer keys and access tokens, used for OAuth
consumer_key = REDACTED
consumer_secret = REDACTED
access_token = REDACTED
access_token_secret = REDACTED

url = "https://www.google.com/search?&q=site%3Atwitter.com+The+latest+Tweets+from+%22{0}%22&oq=site%3Atwitter.com+The+latest+Tweets+from+%22{1}%22&start={2}"
listOfInfo = {'James': [u'JKCorden', u'jkcorden', u'Lileks', u'jamesblake', u'media', u'KingJames', u'vicegandako', u'JayeHanash', u'realellsworth', u'latelateshow', u'JamesTWmusic', u'CricketAus', u'JamzGarner', u'ASICSaustralia', u'jharrison9292', u'media', u'jen13t', u'JimCameron', u'keyframes', u'TheGujaratLions', u'StephenCurry30', u'Comey', u'Crickettas', u'JamesArthur23', u'JamesFaulkner44', u'FBI', u'font', u'Gray_Nicolls', u'StarsBBL', u'comey', u'font', u'nytimes', u'XplodingUnicorn', u'bbctms', u'media', u'jimmy9', u'keyframes', u'JamesFallows', u'joel_jessee', u'creepypuppet', u'JamesBlunt', u'MrJamesMay', u'jamesdashner', u'JamesBayMusic', u'poniewozik', u'JamesMorrisonOK', u'SkyNews', u'keyframes', u'SpaderIsland', u'nbc', u'font', u'bbcproms', u'THEJamesWhale', u'BBCFOUR', u'media', u'StaxRecords', u'RoyalAlbertHallpic', u'JamesPurefoy', u'jbro_1776', u'talkRadio', u'RoyalAlbertHall', u'JamesBlunt', u'ThisIsLafferty', u'NewMediaCentral', u'EDGTVshow', u'Jbrower85', u'TheVampsJames', u'wearejames', u'RoJamesXIX', u'Snowden', u'jamesmaslow', u'TeamJR10', u'media', u'50Latersbaby', u'MLG_Rocks', u'keyframes', u'realDonaldTrump', u'FreedomofPress', u'StephenCurry30', u'JamesTaylor_com', u'jamesdrodriguez', u'Comey', u'font', u'E_L_James', u'fjamie013', u'KingJames', u'media', u'VidiotsOnline', u'JamesMarstersOf', u'Sethrogen', u'keyframes', u'BoringMilner', u'jginorton', u'Comey', u'JamesGunn', u'font', u'OliverPhelps', u'veitchtweets', u'JamesMartinSJ', u'BradleyJames', u'VaticanNews', u'jamestaranto', u'JamesWolk', u'media', u'UberHaxorNova', u'keyframes', u'jamescaan', u'Americamag', u'jamesdoleman', u'JHarden13', u'font', u'orengo_james', u'JamesPMorrison', u'thegreat__4', u'coachjfranklin', u'JP_Books', u'media', u'japastu', u'JRBlake', u'keyframes', u'Lawrence', u'jaltucher', u'jameslabrie', u'revjamesrobison', u'font', u'JHill_Official', u'EarthUncutTV', u'britjfrain', u'MrJamesMay', u'canyonjim', u'JeremyClarkson', u'media', u'GaryLineker', u'jamesdrodriguez', u'YouTube', u'keyframes', u'Bajszi1', u'JamesUrbaniak', u'StephenCurry30', u'TEDTalks', u'Jamesalinn1', u'JamesArthur23', u'font', u'JRhodesPianist', u'JamesASupport', u'BBC_TopGear', u'Uber', u'mrjamesob', u'SenatorLankford', u'jamesmacm', u'jamesMday', u'ZO2_', u'media', u'JamesLaRosa', u'keyframes', u'James_Phelps', u'JimMFelton', u'JamesVictore', u'iflscience', u'font', u'KyleKuzma', u'TheCumnockTryst', u'DurbinRock', u'KYComer', u'mang0ld', u'media', u'jameyperrenot', u'JamesRosenTV', u'keyframes', u'JamesGRickards', u'StephenAtHome', u'SMGrecordsMedia', u'js7', u'JamesPearceEcho', u'MickieJames', u'gasawaymusic', u'font', u'The_JamesJordan', u'TiffanyAlexis04', u'MarkRamprakash', u'jamestaylor20', u'itsjameskennedy', u'media', u'KingJames', u'jbairstow21', u'PVeritas_Action', u'keyframes', u'jgryall', u'JamesOKeefeIII', u'Clyburn', u'TheoJNews', u'JimFetzer', u'james_clear', u'font', u'root66', u'Project_Veritas', u'SuperStopGap', u'RSI', u'Nigelrefowens', u'dcexaminer', u'media', u'CatholicUniv', u'AnnCoulter', u'keyframes', u'DrJamesPeterson', u'FrankieJGrande', u'AmericanU', u'007', u'JamesStormBrand', u'JAllenMc', u'jiwallner', u'jcorrigangolf', u'James_J_Devine', u'LawLiberty', u'font', u'nickknowles', u'JamesWolcott', u'WashingtonPost', u'JimLaPorta', u'jameswisniewski', u'media', u'spann', u'jameshaskell', u'jamesdolemann', u'keyframes', u'TheDailyBeast', u'MrJamesCosmo', u'JamesConner_', u'JamesBlunt', u'NYTimes', u'jfoleyjourno', u'font', u'SenPaterson', u'BoldyJames', u'DrJamesCDobson', u'JamesLock__', u'media', u'keyframes', u'TylerJamesWill', u'JamesDukeMason', u'JamesWade180', u'jamesaknight', u'font', u'Jamesleonard87', u'USMC', u'JamesFrankwin', u'media', u'AtlanticCouncil', u'JJCarafano', u'DrOakley1689', u'keyframes', u'KevinJames', u'OTBTweets', u'DrJJoyner', u'JoeNBC', u'jameszabiela', u'font', u'JamieandAngie', u'jameshohmann', u'jimgrueistweet', u'JamesKavanagh_', u'media', u'JamesTurnerYT', u'jimjames', u'jamesdegale1', u'keyframes', u'ElivsBailey', u'jamesrollins', u'JamesJeanArt', u'GreekCatholic', u'font', u'YorkHistoryDept', u'benshapiro', u'DJMHarland', u'jroberts332', u'NBAalumni', u'popeofwelding', u'JamesAALongman', u'James_Iha', u'media', u'JamesCostos', u'vanderjames', u'keyframes', u'HOLATV', u'eceti', u'JMcCarthy_16', u'font', u'JamesWorthy42', u'TheVampsband', u'AP_Politics', u'JamesDysonAward', u'Vasanthan_James', u'media', u'_jamespattinson', u'keyframes', u'mrjamesholden', u'JAMESSELFE3', u'BigTicket_JW', u'davidfrum', u'NBA', u'font', u'JamesMcC_14', u'LIL_ICEBUNNY', u'jamesbarkerband', u'font', u'JamesGrantFL', u'SweetFeet_White', u'margot_james_mp', u'media', u'PickMyYA', u'CareSync', u'keyframes', u'IamJamesScott', u'kobebryant', u'jamescfox', u'jameshamblin', u'donttelltales', u'JamesMTilton'], 'Mary': [u'News_St_Marys_B', u'media', u'SuprMaryFace', u'maryjblige', u'iamqueenlatifah', u'peacewillfollow', u'marykarrlit', u'GM', u'keyframes', u'marynorwood', u'AmericanHotLips', u'font', u'mtbarra', u'marylambertsing', u'maryregina11', u'angry_gram', u'marycmccormack', u'MaryMcDonnell10', u'therichardlewis', u'media', u'marymclennan', u'MaryHobin', u'keyframes', u'yokoono', u'brianrayguitar', u'donovanofficial', u'cubewatermelon', u'marygauthier_', u'font', u'mary', u'anytimeatall_', u'MaryRobinette', u'williamandmary', u'MangteC', u'AWPArocks', u'MaryKassian', u'media', u'CSTEPS_ASU', u'keyframes', u'NPRKelly', u'AngelCardReader', u'sciwriter', u'mkfeeneyWYO', u'Paragsatpic', u'font', u'NPR', u'MaryMatiella', u'mjoehlerich', u'MaryGioiaGrace', u'media', u'itsmaryk', u'keyframes', u'MaryLeeShark', u'mkayandrews', u'marykmac', u'font', u'marymargaretmay', u'marycrasto', u'shipwrckdcomedy', u'maryohara1', u'NewYorker', u'TheLBDOfficial', u'NkemdiMary', u'mkwiles', u'media', u'marypilon', u'sapphicgeek', u'jonezy89mcfc', u'VirtualCameron', u'waywardguide', u'TeamSmella23', u'Pontifex', u'keyframes', u'MountsMary', u'mary_roach', u'font', u'maryheat', u'USAHockey', u'L7sville', u'StMaryAvon', u'MaryMyatt', u'MaryCreaghMP', u'ImEricaCampbell', u'merphie', u'StMaryOTMS', u'media', u'mitchelloconnor', u'keyframes', u'ADWCathSchools', u'maryportas', u'lovee_maryy', u'therealmarymary', u'font', u'_MaryPierce', u'NatalieMerchant', u'M_CCarpenter', u'Wolf_Trap', u'MaryEmilyOHara', u'media', u'marylattimore', u'keyframes', u'SenLandrieu', u'MaryAnnAhernNBC', u'lpm1960', u'MDoriaRussell', u'MSNBC', u'font', u'IamEnidColeslaw', u'MaryGui', u'heymaryann1', u'SpelmanPres', u'little_mavis', u'wwnorton', u'NewYorker', u'maryvalentyne', u'bneri55', u'media', u'MARYMHOFFMAN', u'keyframes', u'holyivy', u'mary_white33', u'This_girlslife', u'Beauty212', u'marypcbuk', u'font', u'MaryNorrisTNY', u'Fran_Neena20409', u'argumatronic', u'marybirdsong', u'marydudziak', u'media', u'keyframes', u'_maryayers', u'TDSB_MSPS', u'SHAFRhistorians', u'mkhammer', u'suga_mani_', u'font', u'marykiria', u'thecustoms', u'TheTroubadour', u'StMarysU', u'MaryPatFlynn1', u'media', u'wmarybeard', u'keyframes', u'MaryLynnRajskub', u'aqcrutchfield', u'MaryLDixon', u'maryT_money', u'MaryT_Money', u'font', u'realDonaldTrump', u'MaryBlackSinger', u'marylenaburg', u'MaryMitchellCST', u'maryfduffy', u'MarySchmich', u'media', u'MaryKayHenry', u'suntimes', u'MCMarykom', u'keyframes', u'wasmaz', u'thescofieldmag', u'maryxm08', u'joanbushur', u'BioMaryKirby', u'choiceofgames', u'font', u'73rdraisin', u'marylarade', u'LewisCJUSD', u'MaryCummins1', u'ProudMaryMovie', u'media', u'MARYMCCREERY1', u'keyframes', u'maryrose_x3', u'MaryWardCentre', u'TherealTaraji', u'mholland85', u'font', u'marykd7', u'lipetz_mary', u'monkeypat', u'MarySpio', u'coughlanmary', u'maryannegibbs45', u'media', u'ember_dog', u'keyframes', u'HOTtamaleTRAIN', u'missmaryberry', u'ConnectedTruth', u'ramdonomo', u'font', u'UMHB', u'mary_grace', u'jermops', u'TheQueenMary', u'MaryHanburyNYC', u'media', u'GovMaryFallin', u'keyframes', u'MaryJoPehl', u'RMSQueenMary2', u'marybschneider', u'RiffTrax', u'MarySteenburgen', u'itsamarython', u'font', u'Dooezer', u'marymurrah', u'AstralColt', u'Bristolmary', u'media', u'keyframes', u'WMTribeMBB', u'maryamccartney', u'Maryrey88853148', u'MaryEMcGlynn', u'MaryDimx', u'MaryChayko', u'font', u'maryengelbreit', u'MaryLangerThomp', u'The_RSAW', u'maryrboyle', u'BPWrigleyville', u'keyframes', u'font', u'womenref', u'QuickesCheese', u'marydugganarc', u'media', u'myfriendmary', u'THTAudio', u'marmurray', u'RIBApic', u'MICDS', u'mary_mermar', u'BtBScore', u'marymcraig', u'MaynoothUni', u'Mishwood1', u'landlordtweets', u'Hardball_Times', u'baseballpro', u'teachingcodex', u'marymackcomedy', u'marymorrissey', u'Mary_Bridge', u'media', u'marybeth181124', u'mmekus97', u'keyframes', u'maryoleary07', u'marysasson', u'WMTribeXCTF', u'chrisduce', u'font', u'MaryTheGeek', u'MaryCorrales_A1', u'bigmarycollatin', u'maryhalton', u'statesman', u'm_catherine719', u'maryohara1', u'media', u'marymhuber', u'keyframes', u'VeryMaryGray', u'PhysicsatQM', u'npt8', u'MaryBaldwinU', u'MaryMMouser', u'MaryLauraPh', u'font', u'MarySarahSnaps', u'mkhammer', u'NBCTheVoice', u'mkcary', u'_maryfucci', u'media', u'hansen_mary', u'keyframes', u'DivintyMary', u'BiPodisan', u'MaryMeltonLA', u'MetOpera', u'MarySarahMusic', u'PopUpMag', u'font', u'GatorMary', u'THEMaryoga', u'MMaryMcKenna', u'marycjordan', u'spaceparentsbsg', u'batsgirl', u'marychanx', u'MissMaryyMac', u'media', u'keyframes', u'sciarc', u'mary_franck', u'marianmopas', u'MaryFreakingMcD', u'font', u'MaryNicholsCA', u'MaryKay']}

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def cleanTweet(tweetText):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweetText).split())

def extractTwitterHandles(text):
	return list(set(re.findall("(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z0-9_]+)", text)))

def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def grabAllUsers():
	for i in range(20):
		res = grabSite(url.format("Mary", "Mary", i*10))
		userNames = extractTwitterHandles(res.text)
		for user in userNames:
			print user
			allUserNames["Mary"].append(user)
		time.sleep(5)
	for i in range(20):
		res = grabSite(url.format("James", "James", i*10))
		userNames = extractTwitterHandles(res.text)
		for user in userNames:
			print user
			allUserNames["James"].append(user)
		time.sleep(5)
	print allUserNames

def grabAllMale(name="James"):
	for i, userName in enumerate(listOfInfo[name]):
		print("{} / {}".format(i, len(listOfInfo[name])))
		try:
			for status in tweepy.Cursor(api.user_timeline, wait_on_rate_limit=True, screen_name='@{}'.format(userName)).items(50):
				maleTweets.append(cleanTweet(status._json["text"]))
			print(userName)
		except:
			pass

def grabAllFemale(name="Mary"):
	for i, userName in enumerate(listOfInfo[name]):
		print("{} / {}".format(i, len(listOfInfo[name])))
		try:
			for status in tweepy.Cursor(api.user_timeline, wait_on_rate_limit=True, screen_name='@{}'.format(userName)).items(50):
				femaleTweets.append(cleanTweet(status._json["text"]))
			print(userName)
		except:
			pass

#url = 'https://www.google.com/search?&q=site%3Atwitter.com+The+latest+Tweets+from+%22Mary%22&oq=site%3Atwitter.com+The+latest+Tweets+from+%22Mary%22'
if __name__ == '__main__':
	grabAllMale()
	grabAllFemale()
	f = open("femaleText.txt", "w")
	f.write('\n'.join(femaleTweets))
	f.close()
	f = open("maleText.txt", "w")
	f.write('\n'.join(maleTweets))
	f.close()


