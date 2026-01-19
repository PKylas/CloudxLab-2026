#! /usr/bin/python3

def point_on_line(a,p):
    if (a[0] and a[1] > 0):
        if(p in range(a[0], a[1])):
            return "True"
        else:
            return "False"
    elif(a[0] < 0 and a[1] > 0):
        if(p <= a[1] and p >= a[0]):
            return "True"
        else:
            return "False"
    elif(a[1] < 0 and a[0] > 0):
        if(p <= a[0] and p >= a[1]):
            return "True"
        else:
            return "False"
    elif(a[0] and a[1] < 0):
        if(a[0] > a[1]):
            return "True" if(p <= a[0] and p >= a[1]) else "False"
        else:
            return "True" if(p <= a[1] and p >= a[0]) else "False"
        

a1 = input("Please enter a pair of coordinates separated by a blank space: ")
a1 = tuple(map(int, a1.split()))
p1 = input("Please enter the value for a point on a line: ")
p1 = int(p1)

res = point_on_line(a1, p1)
print(f"Is point {p1} on the line {a1}:", res)