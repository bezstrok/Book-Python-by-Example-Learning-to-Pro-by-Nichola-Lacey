"""
Update
program 056
so that it
tells the
user if they
are too high
or too low
before they
pick again.
"""

import random

num = random.randint(1, 10)

guess = int(input("Please enter a number: "))

while guess != num:
	if guess > num:
		print("Too high")
	else:
		print("Too low")
	
	guess = int(input("Please enter a number: "))

print("You won!")
