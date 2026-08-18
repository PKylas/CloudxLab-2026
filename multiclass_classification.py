#! usr/bin/python3

import os
from openai import OpenAI
import pandas as pd
import numpy as np
from collections import Counter


with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"]=openai_key

def euclidean(feature_row, data_row):
    total = 0.0
    for i in range(len(feature_row)):
        total += (feature_row[i]-data_row[i])**2
    return total ** 0.5

def get_neighbors(feature, target, data, k):
    distances=[]
    for i in range(len(feature)):
        dist = euclidean(feature[i], data)
        distances.append((target[i], dist))
    
    distances.sort(key=lambda x: x[1])    
    return distances[0:k]


def classify(feature, target, data, k):
    neighbors = get_neighbors(feature, target, data, k)
    vote_count = [tuple(ballot[0]) for ballot in neighbors]
    frequencies = Counter(vote_count)
    first_key = next(iter(frequencies))
    flora = "Iris Setosa" if first_key[0] == 1 else ("Iris Versicolor" if first_key[0] == 2 else "Iris Virginica")
    return flora

if __name__ == "__main__":
    iris_features = pd.read_csv("/Users/prabhakylas/Documents/Datasets/iris_ml.csv").iloc[:,:-1]
    iris_target = pd.read_csv("/Users/prabhakylas/Documents/Datasets/iris_ml.csv").iloc[:,[-1]].to_numpy().tolist()

    # print(list(iris_features.columns))
    iris_ft_2d = iris_features[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].to_numpy().tolist()
    # print(iris_ft_2d[0:5])
    # print(iris_target[0])
    
    new_data = input(f"Enter sepal length, sepal width, petal length, and petal width:\n").split()
    k = 3
    data = [float(item) for item in new_data]
    flower = classify(iris_ft_2d, iris_target, data, k)
    print(flower)



