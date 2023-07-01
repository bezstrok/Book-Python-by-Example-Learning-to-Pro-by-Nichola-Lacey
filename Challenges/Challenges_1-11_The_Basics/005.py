"""
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer].
"""

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

print(f"The answer is {(num1 + num2) * num3}")
