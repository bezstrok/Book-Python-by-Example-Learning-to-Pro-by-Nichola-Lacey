"""
Draw a triangle.
"""

import turtle

angle = 120

for _ in range(3):
	turtle.forward(100)
	turtle.right(angle)

turtle.exitonclick()
