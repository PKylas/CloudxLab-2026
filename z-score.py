#! /usr/bin/python3

import math

def find_outliers(a, threshold):
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
    print(f"Avergae is {avg} and standard deviation is {sd}")
    # Find the z-score and return the outliers
    for i in range(len(a)):
        z_score = ((a[i]-avg)/sd)
        if z_score >= threshold:
            return a[i]


        
data = input("Please enter some numbers separated by a blank space: ")
data = tuple(map(int, data.split()))
threshold = int(input("Please enter a threshold number: "))

res =[]
res = find_outliers(data, threshold)
print(res) 