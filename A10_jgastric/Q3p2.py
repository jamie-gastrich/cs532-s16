import requests
import json

listID = []
listCount = []

links = open('Links.txt', 'r+')
mementos = open('./twitterJunk4.txt' , 'a+')


for urlLine in links:
    count = 0

    res = requests.get('http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/' + urlLine)

    linkFile = open('Links.txt', 'w+')
    linkFile.write(res.text)
    linkFile.close()
    linkFile = open('Links.txt', 'r')
    for line in linkFile:
        if line:
            if 'rel="memento"' in line or 'rel="memento first"' in line or 'rel="memento last' in line:
                count += 1
    mementos.write(str(count) + '\n')
    if count in listID:
        for index, value in enumerate(listID):
            if value == count:
                listCount[index] += 1
    else:
        listID.append(count)
        listCount.append(1)
for fillslot in range(len(listID)-1,0,-1):
    positionOfMax=0
    for location in range(1,fillslot+1):
        if listID[location]>listID[positionOfMax]:
            positionOfMax = location

    temp = listID[fillslot]
    listID[fillslot] = listID[positionOfMax]
    listID[positionOfMax] = temp

    temp = listCount[fillslot]
    listCount[fillslot] = listCount[positionOfMax]
    listCount[positionOfMax] = temp         
for index, value in enumerate(listID):
    print str(listID[index]) + ": " + str(listCount[index])
    mementos.write(str(listID[index]) + ": " + str(listCount[index]) + "\n")
