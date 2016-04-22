import feedparser
import re
import urllib
from bs4 import BeautifulSoup 
from urllib import urlopen

def getwordcounts(url):
  # Parse the feed
  d=feedparser.parse(url)
  wc={}
  count = 0
  print(len(d.entries))
  for e in d.entries:
    if 'summary' in e: summary=e.summary
    else: summary=e.description
    words=getwords(e.title+' '+summary)
    for word in words:
      wc.setdefault(word,0)
      wc[word]+=1
  return d.feed.title,wc
apcount={}
wordcounts={}
filename1 = r"Blog.txt"
feedlist=[]
for line in open(filename1):
	feedlist.append(line)
for feedurl in feedlist:
  try:
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word,count in wc.items():
      apcount.setdefault(word,0)
      if count>1:
        apcount[word]+=1
  except:
    print('Failed to parse feed %s' % feedurl)
print(len(apcount))
filename2 = r"RawRSS.txt"
out=open(filename2,'w')
response = urllib.urlopen(feedlist[0])
soup = BeautifulSoup(response, 'html.parser')
out.write(str(soup.encode("utf-8")))

