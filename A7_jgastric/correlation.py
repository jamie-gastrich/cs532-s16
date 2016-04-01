from data_extractor import read_data_files
import argparse 
import logging
import threading  
import sys
import os
import math 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M:%S',filename='correlation.log',filemode='w')
defaultLogger = logging.getLogger('default')
# This is from page 26 of the programming collective intelligence book
def get_prefs(dataList,itemList,userList):
	'''Create a dictionary of people and the movies that they have rated. 
	'''
	movies = {}
	for movie in itemList:
		movie_id = int(movie['movie_id'])
		movie_title = movie['movie_title']
		movies[movie_id] = movie_title
	prefs = {}
	for dataPoint in dataList:
		user_id = int(dataPoint['user_id'])
		movieId = int(dataPoint['item_id'])
		rating = dataPoint['rating']
		prefs.setdefault(user_id,{})
		prefs[user_id][int(movieId)] = float(rating)
	return prefs
#This code is from the recommendations.py file
def sim_pearson(prefs,p1,p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

#This Code is from: http://stackoverflow.com/questions/16063839/scipy-pearsons-correlation-returning-always-1
def user_correlation(userId,dataList,userList,itemList,result,pref_list): 
	correlationCoefficients = []
	for user in userList:
		correlationCoefficients.append({'user_id':user['user_id'],'correlation_coefficent':sim_pearson(pref_list,userId,user['user_id'])})
	result[userId] = sorted(correlationCoefficients,key=lambda x: x['correlation_coefficent'],reverse=True)
	
def printResults(userId,correlationCoefficents):
	topFiveMostCorrelated = correlationCoefficents[:5]
	topFiveLeastCorrelated = correlationCoefficents[len(correlationCoefficents) - 5:]
	heading1 = 'Correlation for: user {userId}'.format(userId=userId)
	print('{heading:-^54}'.format(heading=heading1))
	# Print top five correlated 
	print('{heading:-^54}'.format(heading='Top Five Correlated'))
	for i in range(len(topFiveMostCorrelated)):
		print('{rank}){uid:.<48}{correlation_coeffient:<+5}'.format(rank=i+1,uid=topFiveMostCorrelated[i]['user_id'],correlation_coeffient=topFiveMostCorrelated[i]['correlation_coefficent']))
	# Print bottom five correlated 
	print('{heading:-^54}'.format(heading='Bottom Five Correlated'))
	for i in range(len(topFiveMostCorrelated)):
		print('{rank}){uid:.<48}{correlation_coeffient:<+5}'.format(rank=i+1,uid=topFiveLeastCorrelated[i]['user_id'],correlation_coeffient=topFiveLeastCorrelated[i]['correlation_coefficent']))
	print(54*'-')
	print(54*'-')
if __name__ == '__main__':
    topratingsCount = int(sys.argv[1])
    ratingsfile = sys.argv[2]
    namesfile = sys.argv[3]
    ratingsdict = getRatingsFromFile(ratingsfile)
    averagelist = getAverageRatings(ratingsdict)
    topN = getTopN(averagelist, topratingsCount)
    namesdict = getMovieNames(namesfile)