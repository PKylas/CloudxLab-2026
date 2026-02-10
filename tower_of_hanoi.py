#! /usr/bin/python3


def tower_of_hanoi(x):
    ans = counter = temp = 1
    sum = 0
    while(temp < x):
        counter*=2
        temp+=1
        sum+=counter
    sum+=1
    return(sum)

a = "tower A"    
aux = "tower B"
target = "tower C"
x = int(input("Please enter the number of towers: ")) 
res = tower_of_hanoi(x)

print(f"Minimum moves to solve {x} towers: ", res)
