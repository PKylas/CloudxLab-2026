#! /usr/bin/python3

import math

def distance_2d(x1, y1, x2, y2):
    a = abs(x1-x2)
    b = abs(y1-y2)
    return(a+b)


x1, y1, x2, y2 = [float(i) for i in input("Please enter two pairs of x,y coordinates: ").split()]

res = 0
res = float(res)
res = distance_2d(x1, y1, x2, y2)
print("\nThe Manhattan distance is: ",res)