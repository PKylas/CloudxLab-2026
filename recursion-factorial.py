#! /usr/bin/python3

def factorial(x):
    return (x*(x-1))
    

x = int(input("Enter a number: "))
res = 1
res = int(res)
while(x > 1):
    res=res*factorial(x)
    x-=2

print(res)