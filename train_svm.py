from sklearn import svm
from sklearn.externals import joblib


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

########################################

trainParams = build_params('model/params_train.txt')
validateParams = build_params('model/params_validate.txt')

C = [10, 5, 20]
gamma = [0.03, 0.04, 0.3]
for c in C:
	for g in gamma:
		print '\nC: %f, gamma: %f' % (c, g)
		clf = svm.SVC(C=c, gamma=g)
		print clf.fit(trainParams['x'], trainParams['y'])  
		print clf.score(validateParams['x'], validateParams['y'])  

#joblib.dump(clf, 'model/model.pkl')  
