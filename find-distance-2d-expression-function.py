#! /usr/bin/python3

def distance_2d(x1, y1, x2, y2):
    a = x1-x2
    b = y1-y2
    return((a**2)+(b**2))


x1, y1, x2, y2 = [float(i) for i in input("Please enter two pairs of 2D coordinates: ").split()]

res = 0
res = float(res)
res = distance_2d(x1, y1, x2, y2)
print("\nThe distance is : ", (res**0.5))