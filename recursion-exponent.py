#! /usr/bin/python3

def power(x):
    return x
        
x, y = [int(i) for i in input("Enter two numbers: ").split()]
res = 1
while(True):
    if y >= 1:
      res=res*power(x)
      y-=1
    else:
       break
print(res)