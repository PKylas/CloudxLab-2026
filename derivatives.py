#! /usr/bin/python3
import math

##method-1 with formula
def dy_dx(x, pow):
    return (pow*(x**(pow-1)))

a = 5
pow = 6
x = dy_dx(a, pow)
print(f"Derivative of {a}^{pow} is:", x)

#method-2 factorize to find x^2 in pow
c=0
def factorize(f, factor):
    global c
    if f >= 2:
      f = int(factorize(f/factor, factor))
      c+=1
    return c

a = 5
pow = 6
factor = 2
it = factorize(pow, factor)
for i in range(it):
   x = x+dy_dx(a, i)

print(f"Derivative of {a}^{pow} is:", x)

#derivative of square root of x
def sqrt_dy_dx(x):
    return (math.sqrt(x)/x)

a =7
x = 0.5*sqrt_dy_dx(a)
print(f"Derivative of √{a} is:", x)