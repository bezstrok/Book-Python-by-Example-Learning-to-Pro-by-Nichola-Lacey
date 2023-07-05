"""
Draw a pattern that will change each time the
program is run. Use the random function to pick
the number of lines, the length of each line and
the angle of each turn.
"""

import turtle
import random

for i in range(random.randint(1, 30)):
	turtle.forward(random.randint(25, 100))
	turtle.left(random.randint(1, 365))

turtle.exitonclick()
