#! /usr/bin/python3

def min_max_normalize(a, n):
    min = max = i = 0
    min = a[i]
    max = a[i]
    for i in range(len(a)): 
        if(a[i] < min):
            min = a[i]
        elif(a[i] > max):
            max = a[i]
        i+=1
    res = (n-min)/(max-min)
    return(res)
        
data = input("Please enter some numbers separated by a blank space: ")
data = tuple(map(int, data.split()))
n = float(input("Enter a number from the list that you want to normalize: "))


res = min_max_normalize(data, n)
print("The normalized value is :", res) 