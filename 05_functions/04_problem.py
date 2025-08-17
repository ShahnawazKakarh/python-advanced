# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# Radius of a circle (r) → the distance from the center of the circle to any point on its boundary.
# Area of a circle → how much space the circle covers inside.
# Formula: π × r²
# Example: if radius = 3 → Area = 3.14 × (3 × 3) = 28.26 (approx).
# Circumference of a circle → the total length around the circle (like the perimeter of other shapes).
# Formula: 2 × π × r
# Example: if radius = 3 → Circumference = 2 × 3.14 × 3 = 18.84 (approx).
#  So when you’re “given the radius,” you can use these two formulas to find both area (inside space)
# and circumference (outer boundary length).


def calculate_area(radius):
    # Formula: π × r²
    area = (3.14*(radius**2))
    return area

def calculate_cirumference(radius):
    # Formula: 2 × π × r
    # or
    # d = 2r**2
    # pi = c/d , so, c = pi(2r), which can be c = 2*pi*r
    cirumference = (2*3.14*(radius))
    return cirumference

print(calculate_area(3))
print(calculate_cirumference(3))

# There is another way if we import math and use math.pi and to calculate the area and cirumference.

# ############################################################### #