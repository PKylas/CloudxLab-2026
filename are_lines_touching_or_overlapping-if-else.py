#! /usr/bin/python3

def are_lines_touching_or_overlapping(a,b):
    if abs(b[0]) <= abs(a[1]) or abs(b[1] >= a[1]):
        return "True"
    else:
        return "False" 
        

a1 = input("Please enter two points of a line separated by a blank space: ")
a1 = tuple(map(int, a1.split()))
b1 = input("Please enter two points of a second line separated by a blank space: ")
b1 = tuple(map(int, b1.split()))

res = are_lines_touching_or_overlapping(a1, b1)
print("Do the lines overlap or touch at a point:", res)