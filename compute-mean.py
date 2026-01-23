#! /usr/bin/python3

def compute_mean(a):
    sum = i = 0
    for i in range(len(a)): 
        sum+=a[i]
        i+=1
    res = sum/len(a)
    return(res)
        
data = input("Please enter some numbers separated by a blank space: ")
data = tuple(map(int, data.split()))

res = compute_mean(data)
print("The mean is :", res) 