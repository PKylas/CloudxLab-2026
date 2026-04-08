#! /usr/bin/python3

import os
import numpy as np
from numpy import random

##randomly generate a 5 by 9 array of data
data = np.random.randint(100, size=(9,5))

print(data)

centroids = []

k=3
n = p = 0
#Store index for four random rows from the data. Centroids will be chosen from these rows.
centroid_index = np.random.choice(data.shape[1], size=k, replace=False)

cluster_num={}
j = 0
for i in centroid_index:
     centroids.append(np.median(data[i]))
     cluster_num[j]=centroids[j]
     j+=1

#what is the best rational to compute centroids from a dataset?

print("Centroids:", centroids)

print("Cluster number for each centroid:", cluster_num)

#compute euclidean distance between data points and centroids
distances=[]
list_of_lists = []

def euclidean_distance(data_point, centroid_index):
    return np.sqrt(np.sum((centroid_index-data_point)**2))

for data_point in data: 
   for c_index in centroid_index:
     distances.append(euclidean_distance(data_point, data[c_index]))

 #Convert distances into a list of lists    
n = 3
size = len(distances)
for i in range(0, size, 3):
     # Slice the list from index i to i + n
     slice = distances[i:i+n]
     list_of_lists.append(slice)
         
print("Distance of data points from the centroids:", list_of_lists)
indices = []

#Find the index of the lowest value in each list within lists_of_lists
for i in list_of_lists:
    indices.append(np.argmin(i))

sub_cluster = []
new_cluster=[]

print("Cluster indices to which data points must be added:", indices)

for item in range(k):
  for i in indices:
     if item == indices[i]:
       sub_cluster.append(data[i])
  new_cluster.insert(item, sub_cluster[])
  sub_cluster = []
print(new_cluster)