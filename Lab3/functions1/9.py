import math

def sphere_volume(r):
    return (4/3) * math.pi * (r**3)


radius = 5
print(f"Volume of sphere with radius={radius} is {sphere_volume(radius):.2f}")