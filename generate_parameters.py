from functions import *
from random import shuffle
import csv

csv_file = 'dataset.csv'

params_file1 = 'model/params_train.txt'
params_file2 = 'model/params_validate.txt'
params_file3 = 'model/params_test.txt'


lines = []
with open(csv_file) as csvfile:
	reader = csv.DictReader(csvfile)
	wordDict = load_dict('dict.txt')

	
	i = 0
    
	for row in reader:
		stemmed = stemm(row['SENTENCES'], row['COMPANY A'], row['COMPANY B'])

		stemmed = stemmed.split(' ')

		line = ''
		line1 = ''
		for word in wordDict :				
			if word in stemmed :
				line += str(stemmed.index(word) + 1) + ' '
			else :
				line += '0 '

			line1 += str(stemmed.count(word)) + ' '

		line += line1 + example_result(row['relationship']) + '\n'
		lines.append(line)
		

		if i % 100 == 0:
			print i
	
		i += 1		

	shuffle(lines)

	count_train = 85 * len(lines) / 100
	count_validate = 15 * len(lines) / 100

	print count_train
	print count_validate
	print len(lines)

	fp = open(params_file1 , 'w')
	for i in range(0, count_train - 1):
		fp.write(lines[i])
	fp.close()

	fp = open(params_file2 , 'w')
	for i in range(count_train, count_train + count_validate - 1):
		fp.write(lines[i])
	fp.close()

	fp = open(params_file3 , 'w')
	for i in range((count_validate + count_train), len(lines) - 1):
		fp.write(lines[i])
	fp.close()
