#! /usr/bin/python3

class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def add(self, new_vector):
        new_position = []
        for i, value in enumerate(new_vector.coordinates):
            new_position.append(self.coordinates[i] + new_vector.coordinates[i])
        return tuple(new_position)
    
    def dist(self, distance):
        new_dist = []
        for i, value in enumerate(distance.coordinates):
            a = ((self.coordinates[i] - distance.coordinates[i])**2)
            new_dist.append(a)
        return tuple(new_dist)
    
    def windrate(self, scalar):
        new_pos =[]
        for i, value in enumerate(self.coordinates):
            a = scalar * self.coordinates[i]
            new_pos.append(a)
        return tuple(new_pos)

   
position = (3,4)
position_vector = Vector(position)
move = (-2, 3)
moved = Vector(move)
new_position = position_vector.add(moved)
new_pos = Vector((new_position))
distance = new_pos.dist(position_vector)
print("Original position is:", position)
print("Position by which the person moved:", move)
print("The new position is:", new_position)
print("Distance between the original and new position is:", sum(distance))

wind = (5,3)
wind_vector = Vector(wind)
a = 6
windy_pos = wind_vector.windrate(a)
print("Wind speed per second at x-axis and y-axis is:", wind)
print(f"New position in windy weather after {a} seconds: ", windy_pos)