import math
from math import *

#From page 26 of the book programming collective intelligence
def getRecommendedItems(prefs,itemMatch,user):
 userRatings=prefs[user]
 scores={}
 totalSim={}
 # Loop over items rated by this user
 for (item,rating) in userRatings.items( ):
 # Loop over items similar to this one
 for (similarity,item2) in itemMatch[item]:
 # Ignore if this user has already rated this item
 if item2 in userRatings: continue
 # Weighted sum of rating times similarity
 scores.setdefault(item2,0)
 scores[item2]+=similarity*rating
 # Sum of all the similarities
 totalSim.setdefault(item2,0)
 totalSim[item2]+=similarity
 # Divide each total score by total weighting to get an average
 rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
 # Return the rankings from highest to lowest
 rankings.sort( )
 rankings.reverse( )
 return rankings

movieList=sorted(movies.values(),key=lambda v  : v['erate'],reverse=True)
print ('Top 5 recommendations for films')
for mv in movieList[:5]:
	print(mv['name']+'      Most likely rating:  '+ str(mv['erate']))
print ('\nBottom 5 recommendations for films')
for mv in movieList[-5:] :
	print(mv['name']+'      Most likely rating:  '+ str(mv['erate']))

#Do the math for the correlation
pickedId='259'
 result={}
 # Invert the preference matrix to be item-centric
 itemPrefs=transformPrefs(prefs)
 c=0
 for item in itemPrefs:
 # Status updates for large datasets
 c+=1
 if c%100==0: print "%d / %d" % (c,len(itemPrefs))
 # Find the most similar items to this one
 scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
 result[item]=scores
 return result
 #From page 23 of the book Programming collective intelligence
