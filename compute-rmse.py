#! /usr/bin/python3

import math

def compute_rmse(actual, predicted):
    n = sum = 0
    calc = []
    for i in range(len(actual)):
        n = ((actual[i]-predicted[i])**2)
        sum+=n
    avg = sum/(len(actual))
    return math.sqrt(avg)
        
actual = input("Please enter some numbers separated by a blank space: ")
actual = list(map(int, actual.split()))
predicted = input("Please enter some numbers separated by a blank space: ")
predicted = list(map(int, predicted.split()))
res = 0
res = compute_rmse(actual, predicted)
print("The root mean square error is:", res) 