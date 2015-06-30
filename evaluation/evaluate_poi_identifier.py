#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn import cross_validation 
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
d_tree = tree.DecisionTreeClassifier()
d_tree.fit(features_train, labels_train)
pred = d_tree.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)


'''
#FOR COUNTING TRUE POSITIVES (PART OF MINI-PROJECT)
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for i in range(len(predictions)):
    if(predictions[i]!=true_labels[i] and predictions[i]==0):
        count +=1
print count
'''

'''
#FOR PRECISION RECALL
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

precision = precision_score(labels_test, pred)

recall = recall_score(labels_test, pred)

print precision, recall, float(2*precision*recall)/(precision+recall)
'''    