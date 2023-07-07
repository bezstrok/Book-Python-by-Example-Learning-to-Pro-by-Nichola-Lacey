"""
Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything.
"""

import random
import csv

num_1_1, num_1_2, num_2_1, num_2_2 = [random.randint(1, 99) for _ in range(4)]
answer_1 = num_1_1 + num_1_2
answer_2 = num_2_1 + num_2_2

name = input("Please enter your name: ")
guess_1 = int(input(f"{num_1_1} + {num_1_2} = "))
guess_2 = int(input(f"{num_2_1} + {num_2_2} = "))

with open("Math_Quiz.csv", 'a', newline='') as f:
	writer = csv.writer(f)
	writer.writerow((name, num_1_1, num_1_2, guess_1, answer_1, int(guess_1 == answer_1)))
	writer.writerow((name, num_2_1, num_2_2, guess_2, answer_2, int(guess_2 == answer_2)))
