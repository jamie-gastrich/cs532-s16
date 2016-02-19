import pycurl
import requests
import sys
import lynx
import os
import re
import json
from bs4 import BeautifulSoup

SN = 0
for line in open('Links.txt','r'):
    DN = './doc' + str(i) + '.txt'
    PN = './prodoc' + str(i) + '.txt'
    docs = open(DN , 'w+')
    prodocs = open(PN , 'w+')
    url = str(line)
    url = url[:-1]
    storage = StringIO()
    c = pycurl.Curl()
    c.perform()
    c.close()
    content = storage.getvalue()
    docs.write(content)
    Html = docs.read()
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr,'', Html)
    print cleantext
    prodocs.write(cleantext)
    docs.close()
    prodocs.close()
    print line
    SN = SN + 1
    with open('Jason.json','w')as f:
		json.dump(FNames,f)