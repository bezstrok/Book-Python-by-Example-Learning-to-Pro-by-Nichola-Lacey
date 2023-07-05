"""
Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line.
"""

import turtle

turtle.left(25)

for _ in range(8):
	turtle.forward(100)
	turtle.left(45)

turtle.exitonclick()
