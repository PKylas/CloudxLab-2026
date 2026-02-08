#! /usr/bin/python3

def my_impurity(a,b):
    ## some code
    if a == b:
        return 1.0
    if a ==0 or b == 0:
        return 0.0
    else:
        return (1-(abs(a-b)/(a+b)))


a, b = [int(i) for i in input("Please enter two numbers: ").split()]

res = 0
res = my_impurity(a,b)
print("The impurity is: ", res)