import requests
import json

b=0

mementos1 = open('./twitterJunk1.txt' , 'w+')
mementos2 = open('./twitterJunk2.txt' , 'w+')

for line in open('Links.txt','r'):

    a = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/' + line
    res= requests.get(a)
    test = open('./twitterJunk3.txt' , 'w+')
    i = 0
    test.write(res.text)
    for line in open('twitterJunk3.txt','r'):
        if 'rel="memento"' in line:
            i = i + 1
    b = b + 1
    mementos1.write(str(i) + '\n')
    if i > 0:
        mementos2.write(a + '\n')
    print b
    print i
    print a
