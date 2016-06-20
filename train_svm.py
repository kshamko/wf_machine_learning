from sklearn import svm
from sklearn.externals import joblib
import numpy as np
from functions import *

########################################

trainParams = build_params('model/params_train.txt')
validateParams = build_params('model/params_validate.txt')

param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]

C = [15, 20, 30, 1000]
gamma = [0.03, 0.1, 0.5, 1]

for c in C:
	for g in gamma:
		print '\nC: %f, gamma: %f' % (c, g)
		#decision_function_shape='ovo
		clf = svm.SVC(C=c, gamma=g,decision_function_shape='ovo')
		print clf.fit(np.array(trainParams['x']), np.array(trainParams['y']))  
		print clf.score(np.array(validateParams['x']), np.array(validateParams['y']))  

joblib.dump(clf, 'model/model.pkl')  
