#! /usr/bin/python3


def recursive_divide(dividend, divisor):
    return (dividend-divisor)




dividend, divisor = [int(i) for i in input("Please enter a dividend and a divisor separated by space: ").split()]

counter = 0

if (divisor > dividend and counter == 0):
    res = (0,0)

else:    
    while(True):
     counter+=1
     dividend = recursive_divide(dividend, divisor)
     if((dividend-divisor) < 0):
        break

res = (counter, dividend)
print("The quotient and remainder are:", res)