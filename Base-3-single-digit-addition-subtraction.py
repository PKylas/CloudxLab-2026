#! /usr/bin/python3

base3_1 = {0:"0", 1:"1", 2:"2"}

base3_2 = {0: "00", 1: "01", 2:"02", 3:"10", 4:"11", 5:"12", 6:"20", 7:"21", 8:"22"}

base3_3 = {0: "00", 1: "01", 2:"02", 3:"10", 4:"11", 5:"12", 6:"20", 7:"21", 8:"22"}

x, y = input("Please enter any two digits from 0-2: ").split()

a = int(x) + int(y)

if (a == 0):
    print("The sum in Base 3 is", base3_1[a])
elif (a== 1):
    print("The sum in Base 3 is", base3_1[a])
elif (a == 2):
    print("The sum in Base 3 is", base3_1[a])
else:
    print("The sum in Base 3 is", base3_2[a])

if(x > y):
    b = int(x) - int(y)
else:
    b = int(y) - int(x)

print(f"The difference in Base 3 is {b}")