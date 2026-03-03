#! /usr/bin/python3

import math
from collections import Counter

data = [
    ("Yes", "30000","0", "1",),
    ("Yes", "26000","0", "0",),
    ("Yes", "23000","1", "0"),
    ("No", "14000","1", "1"),
    ("Yes","25500","1", "0"),
    ("No", "12000","0", "1"),
] ## data for accepted job offer in the first column given the compensation, wfh, and nighshift options. 

Features = ["Compensation", "Work from Home", "Nightshift"]

def processdata(data):
    data_processed = []
    for row in data:
        label = row[0]
        features = row[1:]
        data_processed.append((features, label))
    return data_processed

print(len(data[3][0]))

dataset = processdata(data)

def entropy(dataset):
    new_tuple = [row[1] for row in dataset]
    label_count = Counter(new_tuple)
    total = len(dataset)
    p_yes = label_count['Yes']/total
    p_no = label_count['No']/total
    print(f"Probability of accepting job is {p_yes} and probability of rejecting a job is {p_no}")
    entro = ((p_yes * math.log2(p_yes))+ (p_no * math.log2(p_no)))
    print("Entropy is:", entro)
    
entropy_count = entropy(dataset) ##calculate the entropy of the accepted and rejected job offers in the data.

