"""
Display the following menu to the user:
If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.
If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.
Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.
If they do not select a relevant option on the first menu
you should display a suitable message.
"""

import random


def addition():
	num_1, num_2 = (random.randint(5, 20) for _ in range(2))
	answer = num_1 + num_2
	
	guess = int(input(f"{num_1} + {num_2} = "))
	return guess, answer


def substraction():
	num_1, num_2 = random.randint(25, 50), random.randint(1, 25)
	answer = num_1 - num_2
	
	guess = int(input(f"{num_1} - {num_2} = "))
	return guess, answer


def check(guess, answer):
	if guess == answer:
		print("Correct")
	else:
		print(f"Incorrect, the answer is {answer}")


def error():
	print("Invalid option")


def main():
	d = {1: addition, 2: substraction}
	print("1) Addition", "2) Substraction", sep='\n')
	num = int(input("Enter 1 or 2: "))
	res = d.get(num, error)()
	if res is not None:
		check(*res)


main()
