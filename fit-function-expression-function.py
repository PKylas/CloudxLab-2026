#! /usr/bin/python3

def fit(x1, y1, x2, y2):
    if(x1 == x2):
        raise ValueError("x coordinates cannot be equal") 
    m = abs(y2-y1)//abs(x2-x1)
    m =float(m)
    c = y2-(m*x2)
    return(m,c)


x1, y1, x2, y2 = [float(i) for i in input("Please enter two pairs of x-axis and y-axis values: ").split()]

res = ()
res = fit(x1, y1, x2, y2)
print("\nThe slope and y-intercept is: ", (res))