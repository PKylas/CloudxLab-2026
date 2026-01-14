#! /usr/bin/python3

ubase = int(input("Please enter a base number: "))

x, y = input("Please enter any two numbers: ").split()

res = []
summed = i = carry = 0
a = list(map(int, str(x)))
b = list(map(int, str(y)))

a = a[::-1]
b = b[::-1]

len = len(a) if a > b else len(b)
while(i < len):
    summed = a[i] + b[i] + carry
    while(summed > 0):
       temp = summed%ubase
       res.append(temp)
       summed = summed/ubase
       summed = int(summed)
       if(summed < 10):
           carry = summed
           break
    i+=1
    summed = 0

res.append(carry)
final_sum = res[::-1]

final_sum = "".join(map(str, final_sum))
print(f"The sum in Base {ubase} is {final_sum}")

