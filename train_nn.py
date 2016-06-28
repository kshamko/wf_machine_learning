from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer
import cPickle as pickle
from math import sqrt

import numpy as np
from functions import *

########################################
hidden_size = 50
<<<<<<< HEAD
epochs = 500
=======
epochs = 15
params_len = 362

>>>>>>> svm2
trainParams = build_params('model/params_train.txt')

y = []
for y1 in trainParams['y']:
	if y1 == 1:
		y.append([1, 0, 0 ,0])
	elif y1 == 2:
		y.append([0, 1, 0 ,0])
	elif y1 == 3:
		y.append([0, 0, 1 ,0])
	elif y1 == 4:
		y.append([0, 0, 0 ,1])

<<<<<<< HEAD
ds = SupervisedDataSet( 379, 4 )
=======
ds = SupervisedDataSet( params_len, 4 )
>>>>>>> svm2

ds.setField( 'input', trainParams['x'] )
ds.setField( 'target', y )


# init and train

<<<<<<< HEAD
net = buildNetwork( 379, hidden_size, 4, bias = True )
=======
net = buildNetwork( params_len, hidden_size, 4, bias = True )
>>>>>>> svm2
trainer = BackpropTrainer( net,ds )

print "training for {} epochs...".format( epochs )

#trainer.trainUntilConvergence(verbose=True)

for i in range( epochs ):
	mse = trainer.train()
	rmse = sqrt( mse )
	print "training RMSE, epoch {}: {}".format( i + 1, rmse )
	
pickle.dump( net, open('model/model_nn.pkl', 'wb' ))





