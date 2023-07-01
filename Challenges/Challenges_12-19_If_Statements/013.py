"""
Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.
"""
BORDERY: int = 20

num = int(input(f"Please enter the number that is under {BORDERY}: "))

if num < BORDERY:
	print("Thank you")
else:
	print("Too high")
