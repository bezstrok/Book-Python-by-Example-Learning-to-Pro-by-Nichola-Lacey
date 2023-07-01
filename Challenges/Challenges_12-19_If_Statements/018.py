"""
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.
"""

START = 10
END = 20

num = int(input("Please enter a number: "))

if num < START:
	print("Too low")
elif num <= END:
	print("Correct")
else:
	print("Too high")
