"""
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places
"""

from math import pi

radius = int(input("Please enter the radius: "))
depth = int(input("Please enter the depth: "))

volume = depth * pi * radius ** 2

print(round(volume, 3))
