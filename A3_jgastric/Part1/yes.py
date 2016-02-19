import os
import sys
import lynx
import re
import subprocess
import pycurl
import requests
import json
def command(fileName):
	m_fileName = fileName.strip('txt')
	return "lynx -dump -force_html " + fileName + " > " + m_fileName + "lynData.txt"
	n_link_files = {}
for link in linksToFiles.keys():
   	Html = docs.read()
   	cleanr = re.compile('<.*?>')
    	cleantext = re.sub(cleanr,'', Html)
   	print cleantext
   	prodocs.write(cleantext)
    	docs.close()
	with open('Jason2.json','w')as f:
	json.dump(n_link_files,f)
   	prodocs.close()
    	print line
