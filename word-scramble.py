#! /usr/bin/python3

from collections import deque

def factorial(l):
    return(l*(l-1))

def destring(s, n):
   d = deque(s)
   d.rotate(n)
   return"".join(d)

    

def  scramble(string):
    l = len(string)
    length = 1
    while(l > 1):
      length = length*factorial(l)
      l-=2

    print("Possible arrangement of letters:", length)

    index = 0
    for i in range(0, len(string)):
       s = string
       li = list(string)
       if i > 0:
        k = i-1
        li[k], li[i]= li[i], li[k]
        s = "".join(li)
       for j in range(0, len(string)):  
        new_s = destring(s, j)            
        print(new_s, end=" ") 
       print("\n")
             
string = input("Please enter a word: ")

scramble(string)
