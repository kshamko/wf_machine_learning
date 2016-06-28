from sklearn import svm
from sklearn.externals import joblib
from functions import *

clf = joblib.load('model/model_svc.pkl') 


CompanyA = 'Tupy'
CompanyB = 'Volkswagen'
text = "~~~Tupy~~~ entered the Automotive market in 1957, when it signed a contract with ~~~Volkswagen~~~."

#CompanyA = 'Delphi'
#CompanyB = 'TRW'
#text = "From a secular growth perspective, ~~~Delphi~~~'s mix of business contains some of the best features of suppliers such as BWA, ~~~TRW~~~, Autoliv, Harman, and JCI."


params_file = 'model/params_validate.txt'
fp = open(params_file, 'r')

results = {'total': 0, 'ok': 0, 'bad': 0}
result_breakdown = {1: {'t':0, 'p':0}, 2: {'t':0, 'p':0}, 3: {'t':0, 'p':0}, 4: {'t':0, 'p':0}}

for line in fp.readlines() :
	
	x = []
	line = line.split(' ')
	j = 1
	line_len = len(line)
	for p in line :

		if j < line_len :	
			x.append(int(p))
		else: 
			y = int(p.strip('\n'))
		j += 1	

	pred = clf.predict([x])
	
	result_breakdown[y]['t'] += 1
	results['total'] += 1
	if pred[0] == y :
		#if y == 3 or y == 4: print 'supplier'
		result_breakdown[y]['p'] += 1
		results['ok'] += 1
	else:
		
		results['bad'] += 1

print results
print results['ok']*100.0/results['total']
print result_breakdown
fp.close()






#wordDict = load_dict('dict.txt')
#stemmed = stemm(text, CompanyA, CompanyB)
#print stemmed
#params = []

#for word in wordDict :
#	if word in stemmed :
#		params.append(1)
#	else :
#		params.append(0)

#pred = clf.predict([params])

#print  show_relation(pred[0])
