#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
import numpy
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] #reducing the size of training set
#########################################################
### your code goes here ###

from sklearn.svm import SVC
c=10000.0 # this value is tuned, large c is giving more accuracy
                # tried c=10, c = 100, 1000 etc
clf = SVC(kernel='rbf', C=c)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print sum(pred) # as chris is 1,this sum predicted chris emails out of 1700
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc

#########################################################


