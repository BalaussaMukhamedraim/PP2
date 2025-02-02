# Write the definition of a Point class. Objects from this class should have a

# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show() # Output (3, 4)
p2.show() # Output (6, 8)

print("Distance between p1 and p2:", p1.dist(p2))

p1.move(10, 12)
p1.show()  # Output: (10, 12)