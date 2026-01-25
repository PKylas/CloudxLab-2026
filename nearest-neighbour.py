#! /usr/bin/python3

import math

def find_nearest_neighbour(data, target):
    diff = []
    for i in range(len(data)):
        temp = abs(data[i]- target)
        diff.append(temp)
    min = i =0
    min = diff[i]
    for i in range(len(data)):
        if(diff[i] < min):
            ans = data[i]
            min = diff[i]
    return ans

        
data = input("Please enter some numbers separated by a blank space: ")
data = list(map(int, data.split()))
data.sort()
target = int(input("Please enter a target number: "))
res = 0
res = find_nearest_neighbour(data, target)
print(f"The nearest neighbor of {target} is:", res) 