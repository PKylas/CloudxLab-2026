#! /usr/bin/python3

import math

def hypoteneuse(b,h):
    return((b*b)+(h*h))


b, h = [float(i) for i in input("Please enter the base and the height of the triangle: ").split()]

res = 0
res = float(res)
res = hypoteneuse(b,h)
print("The hypoteneuse is: ", res**0.5)