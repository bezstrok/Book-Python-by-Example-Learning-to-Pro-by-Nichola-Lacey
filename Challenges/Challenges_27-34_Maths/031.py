"""
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius2).
"""

from math import pi

radius = int(input("Please enter the radius of circle: "))

print(pi * radius ** 2)
