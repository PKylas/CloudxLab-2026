#! /usr/bin/python3

x = int(input("Please enter a number: "))

res=0
counter=0
base = int(3)

while True:
    n = x%10
    n = n * (base**counter)
    n = int(n)
    res = res+n
    x = x/10
    if x < 1:
        break
    counter+=1

print(res)
