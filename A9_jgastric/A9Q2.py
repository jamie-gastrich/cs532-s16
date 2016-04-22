import docclass
import feedparser
import re
import xlsxwriter

def readfile(feed, fisherclassifier):
	f=feedparser.parse(feed)
	print(len(f))
	count = 0
		fulltext = remove_html_tags(entry['title'])
		title.append(str(fulltext))
		fulltext = fulltext +" " +remove_html_tags(entry['summary'])
		# Print the best guess at the current category
		if count < 51:	
			value = str(fisherclassifier.classify(fulltext))
			print('Guess: '+ value)
			guess.append(value)
			temp = input('Enter Category:')
			print("value: ",temp)
			actual.append(temp)
			fisherclassifier.train(fulltext,temp)
		else:
			value1 = str(fisherclassifier.classify(fulltext))
			print(value1)
			guess.append(value1)		
		print()
def remove_html_tags(data):
  p = re.compile(r'<.*?>')
  return p.sub('', data)
	#data headers
	worksheet.write('A1', 'Title', bold)
	worksheet.write('B1', 'Predicted', bold)
	worksheet.write('C1', 'Actual', bold)
	worksheet.write ('D1', 'cprob', bold)
	worksheet.write ('E1', 'fisherprob', bold)
	row = 1
	col = 0
	filename2 = r'Table1.xlsx'
	workbook = xlsxwriter.Workbook(filename2)
	worksheet = workbook.add_worksheet()
	bold = workbook.add_format({'bold' : 1})
		for name in title:
		worksheet.write_string(row, col, name)
		row += 1
	row1 = 1
	col1 = 1	
	for id in guess:
		worksheet.write_string(row1, col1, id)
		row1 += 1
	row1 = 1
	col1 = 2	
	for id1 in actual:
		worksheet.write_string(row1, col1, id)
		row1 += 1
	workbook.close()
	return c2
c2=docclass.fisherclassifier(docclass.getwords)
c3 = readfile("http://superchicken46.blogspot.com/feeds/posts/default?max-results=100", c2)
value = 'a'
while value == 'a':
	temp = input("value:")
	temp1 = input("category:")
	print("Cprob",c2.cprob(temp,temp1))
	print("Fisherprob",c2.fisherprob(temp,temp1))
	value = input("more")

