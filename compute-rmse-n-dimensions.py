#! /usr/bin/python3

import math

def compute_rmse(actual, predicted):
    n = sum = 0
    for i, x in enumerate(actual):
        n = ((x-predicted[i])**2)
        sum+=n
        n=0
    avg = sum/(len(actual))
    return math.sqrt(avg)

rows = int(input("Please enter the dimension for Root Mean Square Error calculation: "))

for i in range(rows):
    actual = input(f"Please enter list {i} actual values separated a blank space: ")
    actual = list(map(int, actual.split()))

for i in range(rows):
    predicted = input(f"Please enter list {i} predicted values separated a blank space: ")
    predicted = list(map(int, predicted.split()))

res = 0
res = compute_rmse(actual, predicted)
print("The root mean square error is:", res) 