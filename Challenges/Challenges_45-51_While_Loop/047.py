"""
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total.
"""

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

value = num1 + num2

answer = input("Do you want add another number? (y\\n)\n").lower()

while answer == 'y':
	value += int(input("Please enter a number: "))
	answer = input("Do you want add another number? (y\\n)\n").lower()

print(f"The total is {value}")
