"""
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”.
"""

import random

answer = random.randint(1, 5)

guess = int(input("Please enter a number: "))

if guess == answer:
	print("Well done")
else:
	print("Too high" if guess > answer else "Too low")
	
	guess = int(input("Try again: "))
	if guess == answer:
		print("Correct")
	else:
		print("You lose")
