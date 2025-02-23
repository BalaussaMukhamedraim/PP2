# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math

num = int(input("Number of sides: "))
length = float(input("Length of a side: "))
area = (num * pow(length, 2)) / (4 * math.tan(math.pi / num))

print("The area of the polygon is:", round(area, 2))