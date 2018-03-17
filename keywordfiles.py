import sys

for line in sys.stdin:
	link,keywords = line.split('@')
	words = keywords.split(';')
	name=link.split('/')[-1]
	print('Creating '+name.strip()+'.txt')
	file = open('txtfiles/'+name.strip()+'.txt','a')
	for word in words:
		word = word.strip()
		file.write(word+'\n')
