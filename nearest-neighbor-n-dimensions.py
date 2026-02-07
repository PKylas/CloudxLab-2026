#! /usr/bin/python3

import math

def find_nearest_neighbor(point, points):
    sum =0
    n = []
    for i, x in enumerate(points):
      j = sum = 0
      for j in range(len(points[i])):
         temp = int(points[i][j])-int(point[j])
         sum = (sum + (temp**2))
      sq = math.sqrt(sum)
      n.append(sq)

    minimum = min(n)
    min_index = n.index(minimum)

    for i, x in enumerate(points):
       if i == min_index:
          return x



rows = int(input("Please enter the number of data points you want to store: "))

point = points = []
for i in range(rows):
    data = list(map(int,input(f"Please enter data point {i} numbers separated a blank space: ").split()))
    points.append(data)

point = input("Please enter a the coordinates of the point for which you want to fing the nearest neighbors: ")
point = list(map(int,point.split()))


res = find_nearest_neighbor(point, points)
print(f"The nearest neighbor of {point} is:", res) 