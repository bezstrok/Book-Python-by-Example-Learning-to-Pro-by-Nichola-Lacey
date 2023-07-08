"""
Define a subprogram
that will ask the user to
pick a low and a high
number, and then
generate a random
number between those
two values and store it in
a variable called
“comp_num”.
Define another
subprogram that will
give the instruction “I am
thinking of a number…”
and then ask the user to
guess the number they
are thinking of.
Define a third
subprogram that will
check to see if the
comp_num is the same
as the user’s guess. If it
is, it should display the
message “Correct, you
win”, otherwise it should
keep looping, telling the
user if they are too low or
too high and asking them
to guess again until they
guess correctly.
"""

import random


def ask() -> int:
	low = int(input("Please enter a low number: "))
	high = int(input("Please enter a high number: "))
	
	comp_num = random.randint(low, high)
	return comp_num


def instruction() -> int:
	print("I'm thinking of number...")
	guess = int(input("Try to guess: "))
	return guess


def result(guess: int, answer: int) -> bool:
	return guess == answer


def main():
	answer = ask()
	guess = instruction()
	
	while not result(guess, answer):
		if guess > answer:
			print("You are too high")
		else:
			print("You are too low")
		
		guess = instruction()
	
	print("Correct, you win")


if __name__ == '__main__':
	main()
