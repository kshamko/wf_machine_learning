##Task
Classify releation between companies

##Algorithms

Have tried __Support Vectore Machine (SVM)__ and __Neural Network (NN)__ algorithms. __Gaussian kernel__ is used for SVM. __Linear kernel__ gives score of about 0.5

##Usage

To use the code one should install stemming, sklearn, pybrain, numpy, nltk extensions

1. ``$ python process_dataset.py``  
This command will generate dictionary to build ML parameters from. 
2. ``$ python generate_parameters.py``  
This command generates parameters to feed to classifier. Each branch has it's own way of the generation.
Common thing is just splitting entire dataset into 2 parts: learning parameters and validation ones in proportion of 85% / 15%
3. ``$ python train_svm.py (or $ python train_nn.by)``  
This command starts classifier training. After trainig script will output params of classifier and algorithm score
4. ``$ python predict.py (or $ python predict_nn.py )``  
This will output algotithm score + some details 

###Basic Approach To Generate Dict:

There is just a basic description below. Please see the code for more details.

1. Replace company1 and company2 names with "companya" and "companyb"
2. Lower text
3. Remove punctuation and all non-letter characters
4. Remove stop words
5. Stem words
6. Split text into words
7. Add words with occurance count over than 350 into dictionary
8. Use dictionary to generate parameters

##C and Gamma selection (SVM):

Have tried classifier with different C and Gamma parameters. Best fit with C=100, Gamma=0.01
 
##Branches:

Main defference in branches is in a way how learning parameters are generated

####master
#####	Classifier Score: 0.68

Parameters are bags of words i.e  
Sentence 1: "The cat sat on the hat"  
Sentence 2: "The dog ate the cat and the hat"  
From these two sentences, our vocabulary is as follows:  
``{ the, cat, sat, on, hat, dog, ate, and }``  

To get our bags of words, we count the number of times each word occurs in each sentence. In Sentence 1, "the" appears twice, and "cat", "sat", "on", and "hat" each appear once, so the feature vector for Sentence 1 is:	{ the, cat, sat, on, hat, dog, ate, and }

Sentence 1: { 2, 1, 1, 1, 1, 0, 0, 0 }  
Sentence 2: { 3, 1, 0, 0, 1, 1, 1, 1}

####svm1
#####	Classifier Score: 0.69
A bit different dict generation + parameteres just 0 (if dict word NOT in text) or 1 (if dict word in text)
Also NN demo is in this branch. Basically all experiments with NN gave scores from 0.5 to 0.55

####svm2
#####	Classifier Score: 0.66
Parameters generated with respect to occurrences and order of words	

