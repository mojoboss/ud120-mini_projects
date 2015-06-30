#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)  # removes the outlier
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
#print data_dict

### your code below

l = []
for a in data_dict:
    if (data_dict[a]['salary']!= 'NaN' and data_dict[a]['bonus']!= 'NaN'):    
        tup=(data_dict[a]['salary'], data_dict[a]['bonus'], a)
        l.append(tup) 
l.sort(key = lambda x: x[0], reverse = True )
print l


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
