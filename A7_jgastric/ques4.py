import math
from math import *
import scipy
from scipy import stats
from scipy.spatial import distance
users={}
movies={}
linktable={}
#parse rating file
linkfile=open('data_files/u.data')
strline=linkfile.readlines()
for line in strline:
    uid,itemid,rating,_=line.split('\t')
    if itemid not in linktable:
        linktable[itemid]={}
    linktable[itemid][uid]=float(rating)
linkfile.close()
#parse movie file
moviefile=open('data_files/u.item')
strline=moviefile.readlines()
for line in strline:
    tuples=line.split('|')
    movies[tuples[0]]=tuples[1]
moviefile.close()
correlation={}
    print('	Top 5 correlated movies:')
    print('	------------------------')
    for m in  correlationArray[:5] :
        print(movies[m] +'  ( correlation: '+str(correlation[m])+' ) ')

    print('	Bottom 5 correlated movies:')
    print('	---------------------------')
    for m in correlationArray[-5:] :
        print(movies[m]+' ( correlation: '+str(correlation[m])+' ) ')
#calculate correlation
pickedId='168'
print('Favorite Movie: 168|Monty Python and the Holy Grail (1974)|')
print('-----------------------------------------------------------')
recommandate(pickedId)
print
print('Least Favorite Movie: 155|Dirty Dancing (1987)|01-Jan-1987|')
print('-----------------------------------------------------------')
pickedId='155'
recommandate(pickedId)