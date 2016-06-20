from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.modules import TanhLayer

import numpy as np
from functions import *

########################################

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

ds = SupervisedDataSet( 1057, 4 )

ds.setField( 'input', trainParams['x'] )
ds.setField( 'target', y )

net = buildNetwork(1057, 1500, 4, bias = True)
trainer = BackpropTrainer( net, ds )

trainer.trainUntilConvergence( verbose = True, validationProportion = 0.15, maxEpochs = 1000, continueEpochs = 10 )
