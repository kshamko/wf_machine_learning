
import re
from string import punctuation
from stemming.porter2 import stem



def build_params(filename):
	
	fp = open(filename, 'r')

	Xbig = []
	y = []	

	i = 0
	for line in fp.readlines() :
	
		x = []
		line = line.split(' ')
		j = 1
		line_len = len(line)
		for p in line :

			if j < line_len :	
				x.append(int(p))
			else: 
				y.append(int(p.strip('\n')))
			j += 1	
		Xbig.append(x)
		i += 1

	print i
	fp.close()
	return {'x': Xbig, 'y': y}
#############################

def strip_punctuation(s):
	return ''.join(c for c in s if c not in punctuation)

###########################
def dict_stemmed(text, wordDict):

	for word in text.split(' '):    

		if word in wordDict.keys() :
			wordDict[word] += 1
		else:
			wordDict[word] = 1

	return wordDict

##################################
def dict_process(wordDict):
	
	print len(wordDict)
	
	dictList = []
	for word in wordDict:
		if word is not None and wordDict[word] > 100 :
			dictList.append(word)

	return sorted(dictList)



#################################
def save_dict_to_file(wordDict):
	
	print len(wordDict)

	file_name = 'dict.txt'
	f = open(file_name, 'w')

	i = 1
	for word in wordDict:
		f.write( str(i) + '\t' + word + '\n')
		i += 1

	f.close()

def stemm(text, companyA, companyB) :
	companyA = '~~~' + companyA + '~~~'
	companyB = '~~~' + companyB + '~~~'
	stemmed = text.replace(companyA, 'companya ')
	stemmed = stemmed.replace(companyB, 'companyb ')
	stemmed = stemmed.replace('%', 'percent')
	stemmed = stemmed.lower()
	stemmed = re.sub("\d+", "number", stemmed)
	stemmed = re.sub('\s+', ' ', stemmed)
	stemmed = re.sub(r'\W*\b\w{1,2}\b', '', stemmed)
	stemmed = stemmed.replace('  ', ' ')
	stemmed = stemmed.replace('  ', ' ')
	stemmed = stemmed.replace('  ', ' ')
	stemmed = strip_punctuation(stemmed)

	to_return = '';
	for word in stemmed.split(' '):    
		to_return += stem(word) + ' '

	return to_return
 
def example_result(text_result):
	result = '0'

	if text_result == 'No relation exists between the companies' :
		result = '1'
	elif text_result == 'Some direct relation exists between the companies, but is not a valid supplier-customer relation' :
		result = '2'
 	elif text_result == 'B supplies A' :
		result = '3'
	elif text_result == 'A supplies B' : 
		result = '4'

	return result

def show_relation(relation_num):
	relation = 'Relation unclassified'

	if relation_num == 1 :
		relation = 'No relation exists between the companies'
	elif relation_num == 2 :
		relation = 'Some direct relation exists between the companies, but is not a valid supplier-customer relation'
 	elif relation_num == 3 :
		relation = 'B supplies A'
	elif relation_num == 4 : 
		relation = 'A supplies B'

	return relation

############################
def load_dict(filename) :
	wordDict = {};
	dictFile = open(filename, 'r')

	for line in dictFile.readlines() :
		line = line.split('\t')
		wordDict[line[1].strip('\n')] = line[0]

	dictFile.close()
	return wordDict





