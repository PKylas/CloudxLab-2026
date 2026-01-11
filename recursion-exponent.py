#! /usr/bin/python3

def recursion(x):
    if(y == 0):
        return 1
    else:
        return (x)
    

x, y = [int(i) for i in input("Enter two numbers: ").split()]
res = 1
while(y >= 1):
    res=res*(recursion(x))
    y-=1

print(res)