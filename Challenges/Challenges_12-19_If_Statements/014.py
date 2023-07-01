"""
Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.
"""

START: int = 10
END: int = 20

num = int(input(F"Please enter the number between {START} and {END} (inclusive): "))

if START <= num <= END:
	print("Thank you")
else:
	print("Incorrect answer")
