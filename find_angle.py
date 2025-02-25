# ABC is a right triangle, 90 degrere at B.
# Therefore, angle ABC is 90 degree.

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths  AB and BC.
# Your task is to find angle MBC in degrees.

import math

AB = int(input())
BC = int(input())

# Calculate the angle using arctangent (in radians)
theta_radians = math.atan(AB / BC)

# Convert to degrees
theta_degrees = math.degrees(theta_radians)

# Round to the nearest integer
rounded_angle = round(theta_degrees)

# Output with degree symbol using Unicode escape
print(f"{rounded_angle}\u00b0")