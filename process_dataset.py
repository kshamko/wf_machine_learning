#from cement.core.foundation import CementApp
#app = CementApp('process_ds')
#app.setup()
#app.run()

import csv
import re
from string import punctuation

from stemming.porter2 import stem

csv_file = 'dataset.csv';

def strip_punctuation(s):
	return ''.join(c for c in s if c not in punctuation)

###########################
def dict_stemmed(text, wordDict):

	for word in text.split(' '):
    
		if word in wordDict.keys():
			wordDict[word] += 1
		else:
			wordDict[word] = 1

	return wordDict

##################################
def dict_process(wordDict):
	
	print len(wordDict)
	
	dictList = []
	for word in wordDict:
		if wordDict[word] < 20 :
			dictList.append(word)

	return sorted(dictList)

#################################
def saveDictToFile(wordDict):
	
	print len(wordDict)

	file_name = 'dict.txt'
	f = open(file_name, 'w')

	i = 1
	for word in wordDict:
		f.write( str(i) + '\t' + word + '\n')
		i += 1

	f.close()

######################################
######################################

with open(csv_file) as csvfile:
	reader = csv.DictReader(csvfile)
	wordDict = {}

	i = 0
	for row in reader:
		stemmed = row['SENTENCES']
		companyA = '~~~' + row['COMPANY A'] + '~~~'
		companyB = '~~~' + row['COMPANY B'] + '~~~'
		stemmed = stemmed.replace(companyA, 'companya')
		stemmed = stemmed.replace(companyB, 'companyb')
		stemmed = stemmed.replace('%', 'percent')
		stemmed = stemmed.lower()
		stemmed = stem(stemmed)
		stemmed = re.sub("^\d+\s|\s\d+\s|\s\d+$", "number", stemmed)
		stemmed = strip_punctuation(stemmed)

		wordDict = dict_stemmed(stemmed, wordDict)

		if i % 100 == 0:
			print i
	
		i += 1
		

 	words = dict_process(wordDict)
	saveDictToFile(words)




