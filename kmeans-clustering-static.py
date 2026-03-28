#! /usr/bin/python3

import os
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy
import numpy as np
from numpy import random
from sentence_transformers import SentenceTransformer
import chromadb

##randomly generate a 5 by 9 array of data
data = np.random.randint(100, size=(9,5))

print(data)

centroids = []

#Store index for four random rows from the data. Centroids will be chosen from these rows.
centroid_index = np.random.choice(data.shape[1], size=3, replace=False)

cluster_num={}
j = 1
for i in centroid_index:
     centroids.append(np.median(data[i]))
     cluster_num[j]=centroids[j-1]
     j+=1

#what is the best rational to compute centroids from a dataset?

print("Centroids:", centroids) 

#compute euclidean distance
cluster_join = []
distances=[]
j=1

def euclidean_distance(data_point, centroid_index):
    return np.sqrt(np.sum((centroid_index-data_point)**2))

  
for data_point in data:
  for centroid_index in centroids:
     distances.append(euclidean_distance(data_point, centroid_index))
  


print("Distance of data points from the centroids:", distances)

print("Cluster number for each centroid:", cluster_num)