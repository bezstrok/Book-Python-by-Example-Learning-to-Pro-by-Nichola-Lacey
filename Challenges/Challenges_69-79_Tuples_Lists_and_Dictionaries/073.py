"""
Ask the user to
enter four of their
favourite foods
and store them in
a dictionary so
that they are
indexed with
numbers starting
from 1. Display
the dictionary in
full, showing the
index number
and the item. Ask
them which they
want to get rid of
and remove it
from the list. Sort
the remaining
data and display
the dictionary.
"""

d = {}
print("Please enter four foods you like the most:")
for i in range(1, 5):
	food = input().title()
	d[i] = food
print(d)

key = int(input("Which one do you want to get rid of?\n"))
del d[key]

print(d)
