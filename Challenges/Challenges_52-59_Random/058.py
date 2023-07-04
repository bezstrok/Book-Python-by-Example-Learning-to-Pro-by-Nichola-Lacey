"""
Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five.
"""

import random

ROUNDS: int = 5

count = 0

for _ in range(ROUNDS):
	num1, num2 = random.randint(1, 50), random.randint(1, 50)
	guess = int(input(f"{num1} + {num2} == ?\nEnter answer: "))
	
	count += guess == num1 + num2

print(f"Your score is {count} of {ROUNDS}")
