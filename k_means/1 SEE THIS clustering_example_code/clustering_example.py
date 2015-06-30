import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn import preprocessing

####################################
def getData(name):
    l = []
    with open(name) as f:
        for line in f:
            line = line.split()
            l.append( (float(line[0]), float(line[1])) )
    # l is a list of tuples & should be converted to numpy array        
    l = np.reshape(np.array(l), (len(l), 2))
    return l
####################################

#getting data and scaling it     
l = getData('birch1.txt')[:500]
X_scaled = preprocessing.scale(l)

# applying k-means
from sklearn import cluster
# THIS IS THE NUMBER OF CLUSTER CENTROIDS
k=4
centroids, labels, inertia = cluster.k_means(X_scaled, n_clusters=k, n_init=10, max_iter=300)
print centroids
#PLOTTING
colors = ['r', 'b', 'g', 'y']
for i in range(k):
    ds = X_scaled[np.where(labels==i)]
    for j in ds:
        x = j[0]
        y = j[1]        
        plt.scatter(x, y, color = colors[i])
    # This line plots cluster centroids    
    plt.scatter(centroids[i][0], centroids[i][1], s=100, color='black', alpha=1.0)        
plt.show()
################ 


   
'''  
# CURRENT APPROACH
colors = ['r', 'b', 'g', 'y']#the list may contains as many colors
for i in range(k):
    ds = X_scaled[np.where(labels==i)]
    for j in ds:
        x = j[0]
        y = j[1]        
        plt.scatter(x, y, color = colors[i])
    plt.scatter(centroids[i][0], centroids[i][1], s=100, color='black', alpha=1.0)    
 
'''

'''
#100% WORKING more efficient solution

ds = X_scaled[np.where(labels==i)]
# plot the data observations
plt.plot(ds[:,0],ds[:,1],'o')
# plot the centroids
lines = plt.plot(centroids[i,0],centroids[i,1],'kx')
# make the centroid x's bigger
plt.setp(lines,ms=15.0)
plt.setp(lines,mew=2.0)
'''