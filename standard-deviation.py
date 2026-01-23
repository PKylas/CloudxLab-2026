#! /usr/bin/python3

import math

def sd(a):
    sum = n = i = avg = 0
    for i in range(len(a)): 
        sum+=a[i]
        i+=1
    avg = sum/len(a)
    i = 0
    sq = []
    for i in range(len(a)): 
        n = a[i]-avg
        n = n*n
        sq.append(n)
    sum  = i = avg = 0
    for i in range(len(sq)): 
        sum+=sq[i]
        i+=1
    avg = sum/len(sq)
    return(math.sqrt(avg))
        
data = input("Please enter some numbers separated by a blank space: ")
data = tuple(map(int, data.split()))

res = sd(data)
print("The standard deviation is :", res) 