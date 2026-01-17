#! /usr/bin/python3

def distance_3d(x1, y1, z1, x2, y2, z2):
    a = x1-x2
    b = y1-y2
    c = z1-z2
    return((a**2)+(b**2)+(c**2))


x1, y1, z1, x2, y2, z2 = [float(i) for i in input("Please enter two pairs of 3D coordinates: ").split()]

res = 0
res = float(res)
res = distance_3d(x1, y1, z1, x2, y2, z2)
print("\nThe distance in 3D space is : ", (res**0.5))