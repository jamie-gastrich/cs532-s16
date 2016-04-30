import docclass
import feedparser
import re
from sklearn import svm
from sklearn import cross_validation
import numpy as np

def remove_html_tags(data):
  p = re.compile(r'<.*?>')
  return p.sub('', data)
  
def getwords(html):
	txt=re.compile(r'<[^>]+>').sub('',html)
	words=re.compile(r'[^A-Z^a-z]+').split(txt)
	return [word.lower() for word in words if word!='']
def readfile(feed, fisherclassifier):
	title =[]
	guess =[]
	actual=[]
	Yvalue = []
	f=feedparser.parse(feed)
	print(len(f))
	count = 0
	for entry in f['entries']:
		count = count + 1
		print(count)
		print ('-----')
		print ('Title: '+str(entry['title'].encode('utf-8')))
		print()
		fulltext = remove_html_tags(entry['title'])
		title.append(str(fulltext))
		if count < 20:	
			value = str(fisherclassifier.classify(fulltext))
			print('Guess: '+ value)
			if value == 'None':
				Yvalue.append(0)
			else:
				Yvalue.append(int(value))
			temp = raw_input('Enter Category:')
			print("value: ",temp)
			actual.append(int(temp))
			fisherclassifier.train(fulltext,temp)
		else:
			value1 = str(fisherclassifier.classify(fulltext))
			print(value1)
			actual.append(int(temp))
		print()
	return actual
def readVector(filename):
	lines=[]
	for line in open(filename):
		lines.append(line)
	colnames=lines[0].strip().split('\t')[1:]
	rownames=[]
	data=[]
	for line in lines[1:]:
		p=line.strip().split('\t')
		rownames.append(p[0])
		data.append([float(x) for x in p[1:]])
	return rownames,colnames,data
c2=docclass.fisherclassifier(docclass.getwords)
blognames,words,data=readVector('blogdata1.txt')
Yvalue = readfile("http://superchicken46.blogspot.com/feeds/posts/default?max-results=100&alt=rss", c2)
X_digits = np.array(data)
Y_digits = np.array(Yvalue)
clf = svm.SVC(kernel='linear', C=10)
clf.fit(X_digits, Y_digits)
scores = cross_validation.cross_val_score(clf, X_digits, Y_digits, cv = 10)
print(scores.mean())
for i in scores:
	print("Value:", i)
