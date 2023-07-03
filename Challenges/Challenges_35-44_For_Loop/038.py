"""
Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.
"""

name = input("Please enter your name: ")
num = int(input("Please enter number of times: "))

for _ in range(num):
	for l in name:
		print(l)
	print()
