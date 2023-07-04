"""
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.
"""
import random

answer = random.choice(('h', 't'))

guess = input("Please try to guess (t or h): ").lower()

print('You win' if answer == guess else 'Bal luck')

print('It was ' + ('heads', 'tails')[answer == 't'])
