# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

import math

height = float(input("Type height: "))
base1 = float(input("Type the first base: "))
base2 = float(input("Type the second base: "))

area = ((base1 + base2) * height) / 2
print("Area = ", area)