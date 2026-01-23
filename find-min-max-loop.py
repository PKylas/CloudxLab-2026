#! /usr/bin/python3

def find_min_max(a):
    min = max = i = 0
    min = a[i]
    max = a[i]
    for i in range(len(a)): 
        if(a[i] < min):
            min = a[i]
        elif(a[i] > max):
            max = a[i]
        i+=1
    return (min, max)

        
a1 = input("Please enter some numbers separated by a blank space: ")
a1 = tuple(map(int, a1.split()))

res = tuple(find_min_max(a1))
print("The smallest and the largest number are :", res)