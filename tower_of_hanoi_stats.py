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

def breakdown(x):
   m = x
   i = 1
   mo = {}
   while(m >= 1):
       mo.update({m:i})
       m-=1
       i=i*2
   return mo

a = "tower A"    
aux = "tower B"
target = "tower C"
x = int(input("Please enter the number of discs: ")) 
res = tower_of_hanoi(x)

print(f"Minimum moves to solve {x} discs: ", res)

moves = {}

moves = breakdown(x)
print("The disc:number of moves ratio is:", moves)