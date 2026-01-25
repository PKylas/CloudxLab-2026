#! /usr/bin/python3

import math

def find_outliers(a):
    sum = n = i = avg_squared = avg = 0
    # Find the mean of the set of numbers
    for i in range(len(a)): 
        sum+=a[i]
        i+=1
    avg = sum/len(a)
    i = 0
    # Find the standard deviation by deducting the mean from the original set of numbers. 
    # Square the resultant set of values and take the average. 
    # SD is the square root of this average.
    sq = []
    for i in range(len(a)): 
        n = a[i]-avg
        n = n*n
        sq.append(n)
    sum  = i = 0
    for i in range(len(sq)): 
        sum+=sq[i]
        i+=1
    avg_squared = sum/len(sq)
    sd = math.sqrt(avg_squared)
    i = 0
    # Find the z-score 
    std_list=[]
    for i in range(len(a)):
        if sd == 0:
            z_score = 0
        else:
            z_score = ((a[i]-avg)/sd)
        std_list.append(z_score)
    return std_list
        
data = input("Please enter some numbers separated by a blank space: ")
data = tuple(map(int, data.split()))
res =[]
res = find_outliers(data)
print(res) 