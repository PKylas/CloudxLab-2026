#! /usr/bin/python3

def power(x,y):
  if y == 0:
       return 1
  else:
      return x*power(x,y-1)
        
x, y = [int(i) for i in input("Enter two numbers: ").split()]
ans = 1

ans = power(x, y)

print(ans)

