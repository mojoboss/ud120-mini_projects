#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list

temp_counter = 0
for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        #temp_counter += 1
        #if temp_counter < 200:
        path = os.path.join('..', path[:-1])
        email = open(path, "r")
        
        ### use parseOutText to extract the text from the opened email
        emailstr = parseOutText(email)
        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        signature_words = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]
        for sign in signature_words:
            emailstr = emailstr.replace(sign,'')
        ### append the text to word_data
        word_data.append(emailstr)
        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        if (name=='sara'):
            from_data.append(0)
        else:
            from_data.append(1)

        email.close()

print "emails processed\n"
#print word_data[152]
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )




### in Part 4, do TfIdf vectorization here  stop_words='english'

from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
#vectorizer = CountVectorizer()
X = vectorizer.fit_transform(word_data)
#print vectorizer.get_feature_names()
vocab_list = vectorizer.get_feature_names()
'''
(a). X is a scipy sparse matrix, i.e it is denoted in a different notation,
to make it more visual like normal matrices, use X.todense() function.

(b). Also if we use CountVectorizer instead of tfidfVectorizer, then 
fit_transform() in count vectorizer just generates the feature list
(or vocablist) and creates the t-f matrix(what we need is a tf-idf matrix). 
Then after above steps, to create sparse tf-idf matrix, we'll have to use --->

from sklearn.feature_extraction.text import TfidfTransformer
tfidf = TfidfTransformer()
tfidf.fit(X)

this then multiplies tf matrix and idf square matrix to produce tf-idf
matrix.

But in tfidfVectorizer both steps happens with just fit_transform() 
1. so, first approach uses - CountVectorizer & TfidfTransformer
2. and second approach uses - TfidfVectorizer

Results are also normalised in the matrix 
Read - 'http://blog.christianperone.com/?p=1589'
'''
X=X.todense()
print X
print len(vocab_list)
print vocab_list[34597]

