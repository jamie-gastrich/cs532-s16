from data_extractor import read_data_files 
import logging 
# This code is from page 26 of the programming collective intelligence book
def get_prefs(dataList,itemList,userList):
	movies = {}
	for movie in itemList:
		movie_id = movie['movie_id'] 
		movie_title = movie['movie_title']
		movies[movie_id] = movie_title
	prefs = {}
	for dataPoint in dataList:
		user_id = int(dataPoint['user_id'])
		movieId = dataPoint['item_id']
		rating = dataPoint['rating']
		prefs.setdefault(user_id,{})
		prefs[user_id][movies[movieId]] = float(rating)
	return prefs

def get_user_match(name=None,gender=None,age=None,occupation=None):
	# Default values if gender, age or occupation are not passed in.
	_name = 'User'
	_gender = 'M'
	_age = 21
	_occupation = 'student'
	dataList,userList,itemList = read_data_files(dataName='data_files/u.data',itemName='data_files/u.item',userName='data_files/u.user')
	prefs = get_prefs(dataList,itemList,userList) 
	similarUsers = list(filter(lambda x: x['age'] == _age and x['gender'] == _gender and x['occupation'] == _occupation,userList))
	defaultLogger.info("{0} similar users found".format(len(similarUsers)))

def printResults(similarUsers):
	seperator = '-----------------------------------------------------'
	heading0 =  '--------------------Similar Users--------------------'
	heading1 =  '---------------------Top-Three-----------------------'
	heading2 =  '--------------------Bottom-Three---------------------'
	print(heading0)
	for key in similarUsers.keys():
		
		print("User: {0}:".format(key))
		print(heading1)
		counter = 1
		for topThree in similarUsers[key]['top_three_favorite']:
			print("{0}){1:.<48}{2}".format(counter,topThree['movie_title'],topThree['rating']))
			counter += 1
		counter = 1
		print(heading2)
		for bottomThree in similarUsers[key]['bottom_three_favorite']:
			print("{0}){1:.<48}{2}".format(counter,bottomThree['movie_title'],bottomThree['rating']))
			counter += 1
		print(seperator)
		print(seperator)
if __name__ == '__main__':
	gender = None
	age = None 
	occupation = None
	name=None
	occupationFileName = 'data_files/u.occupation'
	try:
		occupationFile = open(occupationFileName,'r')
	except IOError as e:
		defaultLogger.error("Error getting occupation list file: {0},{1}".format(occupationFileName,e[1]))
		print("Error getting occupation list file: {0},{1}".format(occupationFileName,e[1]))