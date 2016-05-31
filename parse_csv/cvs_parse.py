#from __future__ import print_function
import csv
import re

outfile = open('contact.txt', 'w')

with open('contact.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		try:
			row = row[0]
		except IndexError:
			row = ''
		
		row = row.split(",")

		try:
			line=[row[0],row[1],row[25]]
		except IndexError:
			line=['', '', '']

		line = [item.replace('"', '') for item in line]
		line = [item.replace(' ', '') for item in line]
		line = [item.replace('\t', '') for item in line]
		line = [item.replace('\r\n', '') for item in line]
		line = [item.replace('(', '') for item in line]
		line = [item.replace(')', '') for item in line]
		line = [item.replace('-', '') for item in line]
		line = [item.replace('+', '') for item in line]
		
		try:
			line = [item.decode('gb2312') for item in line]
		except UnicodeDecodeError:
			line = line

#		if line[2]!='':
#			print line[0], line[1], line[2]
#			print(line[0]+' '+line[1]+' '+line[2], file=outfile)
		if (line[2].startswith('133') or line[2].startswith('153') 
									or line[2].startswith('189')
									or line[2].startswith('177')
									or line[2].startswith('180')):
			print line[0], line[1], line[2] 
