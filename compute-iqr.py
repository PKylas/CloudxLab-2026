#! /usr/bin/python3

import math

def compute_iqr(data):
    in1 = in2 = 0
    for i in range(len(data)):
        in1 = int((len(data)/4))
        in2 = int(((len(data)*3)/4))
        return(data[in2]-data[in1])
        
data = input("Please enter some numbers separated by a blank space: ")
data = list(map(int, data.split()))
data.sort()
res = 0
res = compute_iqr(data)
print("Interquartile Range of the set of numbers is:", res) 