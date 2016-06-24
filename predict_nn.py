import numpy as np
import cPickle as pickle

from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE

from functions import *

net = pickle.load( open( 'model/model_nn.pkl', 'rb' ))



params_file = 'model/params_train.txt'
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

	pred = net.activate(x)
	res = max(enumerate(pred),key=lambda x: x[1])[0] + 1

	print pred
	print y
	print res
	print '\n'

	result_breakdown[y]['t'] += 1;
	results['total'] += 1
	if res == y :
		#if y == 3 or y == 4: print 'supplier'
		results['ok'] += 1
		result_breakdown[y]['p'] += 1;
	else:
		results['bad'] += 1

print results
print results['ok']*100.0/results['total']
print result_breakdown
fp.close()
