import os
import sys
import subprocess
import json
def command(fileName):
	m_fileName = fileName.strip('txt')
	return "lynx -dump -force_html " + fileName + " > " + m_fileName + "lynData.txt"


def strip_html_from_sources(input_file_name):
	input_file = open('links_to_File_Names.json','r')
	linksToFiles = json.loads(input_file.read())

	n_link_files = {}
	for link in linksToFiles.keys():
		print("Extracting HTML data from: {0}".format(linksToFiles[link]['source_file_name']))
		v = os.popen(command(linksToFiles[link]['source_file_name']))
		m_fileName = linksToFiles[link]['source_file_name'].strip(('.txt'))
		m_fileName = m_fileName + "processed.txt"
		info = {'source_file_name':linksToFiles[link]['source_file_name'], 'stripped_source_file_name': m_fileName }
		n_link_files[link] = info 


	with open('links_to_Files2.json','w')as f:
		json.dump(n_link_files,f)



if __name__== '__main__':
	fName = 'linksToFiles.json'
	strip_html_from_sources(fName)