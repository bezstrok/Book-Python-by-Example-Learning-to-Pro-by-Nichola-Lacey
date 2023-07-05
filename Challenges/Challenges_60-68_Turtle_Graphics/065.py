"""
Write the numbers as shown below,
starting at the bottom of the number
one.
"""

import turtle

turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.pendown()

w, h = 80, 50
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(w)

turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.forward(w)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(w * (2 / 3))
turtle.left(180)
turtle.forward(w * (2 / 3))
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(w)

turtle.exitonclick()
