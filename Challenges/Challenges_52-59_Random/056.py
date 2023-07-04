"""
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.
"""

import random

num = random.randint(1, 10)

guess = int(input("Please enter a number: "))

while guess != num:
	guess = int(input("Please enter a number: "))

print("You won!")
