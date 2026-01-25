#! /usr/bin/python3

def recursion(x):
    return x
        
y = int(input("Enter a number: "))
res = x = 1
while(x <= y):
    res=res*(recursion(x))
    x+=1
print(res)