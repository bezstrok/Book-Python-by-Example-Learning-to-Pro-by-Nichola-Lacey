"""
Draw three squares
in a row with a gap
between each. Fill
them using three
different colours.
"""

import turtle

turtle.penup()
turtle.setx(-(120 * 3 // 2))
turtle.pendown()

for c in ('green', 'yellow', 'pink'):
	turtle.color(c)
	turtle.begin_fill()
	for _ in range(4):
		turtle.forward(100)
		turtle.right(90)
	turtle.end_fill()
	turtle.penup()
	turtle.forward(120)
	turtle.pendown()

turtle.exitonclick()
