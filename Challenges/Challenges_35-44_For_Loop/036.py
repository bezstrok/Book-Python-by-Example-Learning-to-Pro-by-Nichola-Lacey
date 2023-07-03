"""
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.
"""

name = input("Please enter your name: ")
num = int(input("Please enter number of times: "))

for _ in range(num):
	print(name)
