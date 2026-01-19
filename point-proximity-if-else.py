#! /usr/bin/python3

def closer_point(a,b,p):
    result_a = tuple(abs(x-y) for x,y in zip(a, p))
    print(f"Distance between {a} and {p}:", result_a)
    result_b = tuple(abs(x-y) for x,y in zip(b, p))
    print(f"Distance between {b} and {p}:", result_b)

    if(result_a == result_b):
        return "Equal"
    elif(result_a < result_b):
        return "A"
    else:
        return "B"
    

a1 = input("Please enter a pair of coordinates separated by a blank space: ")
a1 = tuple(map(int, a1.split()))
b1 = input("Please enter a pair of coordinates separated by a blank space: ")
b1 = tuple(map(int, b1.split()))
p1 = input("Please enter a pair of coordinates to check for proximity: ")
p1 = tuple(map(int, p1.split()))

res = closer_point(a1, b1, p1)
print(res)