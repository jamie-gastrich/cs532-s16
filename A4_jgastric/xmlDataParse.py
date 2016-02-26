import xml.etree.ElementTree as ET
import sys 
from xml.dom import minidom
import json
def extractFriend(friendNode):
	Friend = {}
	elements = friendNode.getElementsByTagName('data')
	for element in elements:
		Friend[element.attributes['key'].value] = element.firstChild.data
	return Friend
if __name__=='__main__':
	fileName = None
	if len(sys.argv) != 2:
		fileName = 'mln.graphml' # Open given file
	else:
		fileName = str(sys.argv[1])
	data = extract_friend_data(fileName) # extract the data on the file given
	create_plot_data(data)
def create_plot_data(friendData):
	sortedArray = []
	output = []
	output = open('friendsFB.txt','w') # This puts the information in a .txt file
	counter = 0 
	v = sorted(sortedArray,key=lambda x:x[0])
	output.write("id,number_of_friends,name\n")
	for line in v:
		toPrint = str(counter) + ',' + str(line[0]) + ',' + line[1] + '\n'
		output.write(toPrint)
		counter += 1
def extract_friend_data(inputFileName):
graphml = {															#	
"graph": "{http://graphml.graphdrawing.org/xmlns}graph",			#These go through
"node": "{http://graphml.graphdrawing.org/xmlns}node",				#the format
"edge": "{http://graphml.graphdrawing.org/xmlns}edge",				#of the file given
"data": "{http://graphml.graphdrawing.org/xmlns}data",				# and extract all
"label": "{http://graphml.graphdrawing.org/xmlns}data[@key='label']",# the information
"x": "{http://graphml.graphdrawing.org/xmlns}data[@key='x']",		#as given
"y": "{http://graphml.graphdrawing.org/xmlns}data[@key='y']",		#
"size": "{http://graphml.graphdrawing.org/xmlns}data[@key='size']",	#
"r": "{http://graphml.graphdrawing.org/xmlns}data[@key='r']",		#
"g": "{http://graphml.graphdrawing.org/xmlns}data[@key='g']",		#
"b": "{http://graphml.graphdrawing.org/xmlns}data[@key='b']",		#
"weight": "{http://graphml.graphdrawing.org/xmlns}data[@key='weight']",#
"edgeid": "{http://graphml.graphdrawing.org/xmlns}data[@key='edgeid']" #
}
graph = tree.find(graphml.get("graph"))
nodes = graph.findall(graphml.get("node"))
edges = graph.findall(graphml.get("edge"))

	output.close()

