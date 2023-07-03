"""
Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.
"""

name = input("Please enter your name: ")
num = int(input("Please enter a number: "))

if num < 10:
	for _ in range(num):
		print(name)
else:
	print("Too high")
