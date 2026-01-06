#! /usr/bin/python3

x, y = input("Please enter any two numbers: ").split()

a = int(x) + int(y)

a = int(a)

res = []
temp =0

while(a > 0):
    temp = a%3
    res.append(temp)
    a = a/3
    a = int(a)

final_sum = res[::-1]

final_sum = "".join(map(str, final_sum))
print(f"The sum in base 3 is {final_sum}")


if(x > y):
    b = int(x) - int(y)
else:
    b = int(y) - int(x)

res = []
temp =0

while(b > 0):
    temp = b%3
    res.append(temp)
    b = b/3
    b = int(b)

final_diff = res[::-1]
final_diff = "".join(map(str, final_diff))
print(f"The difference in base 3 is {final_diff}")

c = int(x) * int(y)
res = []
temp =0

while(c > 0):
    temp = c%3
    res.append(temp)
    c = c/3
    c = int(c)

final_product = res[::-1]
final_product = "".join(map(str, final_product))
print(f"The product in base 3 is {final_product}")