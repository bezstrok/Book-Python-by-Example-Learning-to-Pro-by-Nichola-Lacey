"""
Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program.
"""

value = 0

while value <= 5:
	value = int(input("Please enter a number: "))

print(f"The last value your entered was {value}")
