import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)


r = float(input("Enter the radius of the sphere: "))
print(f"Volume of the sphere: {sphere_volume(r):.2f}")