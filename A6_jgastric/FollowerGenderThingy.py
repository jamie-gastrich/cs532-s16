import signal
import time 
import json
from gender_detector import GenderDetector
import csv

def find_out_genders(twitterUserData): # figure out genders of users based on user's first name
	detector = GenderDetector('us')
	for screenName in twitterUserData.keys():
		print("Getting gender for: {0} ".format(screenName))
		nam = twitterUserData[screenName]['name']
		toCheck = None
		if nam != '.':
			if " " in nam:
				toCheck = nam.split(" ")[0]
			if toCheck is not None:
				twitterUserData[screenName]['gender'] = detector.guess(toCheck)
			else:
				print(nam)
				twitterUserData[screenName]['gender'] = detector.guess(nam)
	print("Creating backup file:")
	with open('backup2.json','w') as f:
		json.dump(twitterUserData,f)
	print("Results")
	for result in twitterUserData.keys():
		print(result)
		print("\tid: {0}".format(result))
		print("\tscreenName: {0}".format(twitterUserData[result]['screen_name']))
		print("\tgender: {0}".format(twitterUserData[result]['gender']))
	return twitterUserData
def Accounts_without_gender(twitterData): # Deciphers between who has a gender based on the user's first name
	screenNamesToEliminate = []
	for sName in twitterData.keys():
		if twitterData[sName]['gender'] == 'unknown':
			print("{0}: {1}".format(sName,twitterData[sName]['gender']))
			screenNamesToEliminate.append(sName)
	return screenNamesToEliminate
def eliminate_unknown_gender_accounts(userName,twitData): # Eliminates names that have unknown genders
	if twitData[userName]['gender'] == 'unknown' or twitData[userName]['gender'] is None:
		return True  
	else:
		return False 
	newOut = open(newCSVFileName,'w')
	headings = 'source,target,value\n'
	newOut.write(headings)
	for item in newCsvResilts:
		tmp = item[0] + ',' + item[1] + ',1.0\n'
		newOut.write(tmp)
	newOut.close()
	for sName in twitterUsrData.keys(): # creates a table based on the users and the genders
		if eliminateName(sName,twitterUsrData) is not True:
			tmp = twitterUsrData[sName]['screen_name'] + u" & " + twitterUsrData[sName]['name'] + u" & " + twitterUsrData[sName]['gender'] + u' \ \ \hline '
			print(tmp)
		else:
			tmp = twitterUsrData[sName]['screen_name'] + " & " + twitterUsrData[sName]['name'] + u"\ \ \hline "

if __name__=='__main__':
	global twitter_user_data
	kevinFollowers = [] 
	dataFileName = 'userInfo.json'
	twitter_data_file = open(dataFileName,'r')
	twitter_user_data = json.loads(twitter_data_file.readline())
	twitter_data_file.close()
	oldCsvFile = 'network.csv'
	newCsv = 'q2_graph.csv'
	twitterData = determineGenders(twitter_user_data)
	reviseCSV(oldCsvFile,twitterData,newCsv)





