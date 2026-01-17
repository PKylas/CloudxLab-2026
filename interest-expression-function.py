#! /usr/bin/python3

def simple_interest(p, n ,r):
    return((p*n*r)/100)


p, n, r = [float(i) for i in input("Please enter principal, number of years, and rate of interest: ").split()]

res = 0
res = float(res)
res = simple_interest(p, n, r)
print("The simple interest is: ", res)