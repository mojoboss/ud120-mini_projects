#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

# ########SOLVED FOR ENTIRE CHAPTER##############SOLUTIONS COMMENTED


import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

'''
#for calculating poi
count=0
for a in enron_data:
    if enron_data[a]['poi']==True:
        count = count+1
print count
'''

'''
#for getting enron_data keys i.e names of persons
for a in enron_data: 
    print a
'''

'''    
for getting no of persons in "../final_project/poi_names.txt"
with open("../final_project/poi_names.txt") as f:
    count = 1
    for line in f:
        print str(count) + "  " + line
        count+=1
'''

'''
for a in enron_data:
    for val in enron_data[a]:
        print val
    break   
'''


#print enron_data['LAY KENNETH L']['total_payments']

'''
count=0
for a in enron_data:
    for val in enron_data[a]:
        if (val=='email_address' and enron_data[a][val]== 'NaN'):
            count +=1

print count
'''
''' 
count=0
for a in enron_data:
    for val in enron_data[a]:
        if (val=='total_payments' and enron_data[a][val]== 'NaN'):
            count +=1
print count
print count*1.0/len(enron_data )
''' 

'''
count=0
for a in enron_data:
    for val in enron_data[a]:
        if (val=='total_payments' and enron_data[a][val]== 'NaN' and enron_data[a]['poi']== True):
            count +=1
print count
print count*1.0/len(enron_data )
'''