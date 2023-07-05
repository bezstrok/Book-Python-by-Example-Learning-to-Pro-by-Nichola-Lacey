"""
Create the following pattern:
"""

import turtle

angle = 360 // 10

for _ in range(10):
	turtle.left(angle)
	for _ in range(8):
		turtle.left(45)
		turtle.forward(100)

turtle.exitonclick()
