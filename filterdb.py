import sys
import csv

#function to find substring from a string between two given substrings
def find_between( s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

#open file given at command line and remove only relevant links
with open(sys.argv[1],'rb') as f:
	reader=csv.reader(f)
	i=0
	for row in reader:
		if row[2] !='False':  #only public domain images
			if 'India' in '+'.join(row):  #containing word 'India'
				if not('United' in row[31]):  #excluding word 'United' to remove references to Native Indians in United States
					url=find_between('+'.join(row), 'http','+')
					print(row[0]+';'+url)
					#i=i+1
#print(i)


