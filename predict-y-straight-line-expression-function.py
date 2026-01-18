#! /usr/bin/python3

def predict(m, c, x):
    return((m*x+c))


m, c, x = [float(i) for i in input("Please enter the slope, intercept, and x-axis values: ").split()]

res = 0
res = float(res)
res = predict(m, c, x)
print("\nThe y-axis point given the x-axis point with the slope and the intercept is: ", (res))