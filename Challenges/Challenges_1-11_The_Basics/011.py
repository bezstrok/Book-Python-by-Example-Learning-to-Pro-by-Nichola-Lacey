"""
Ask the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.
"""

num1 = int(input("Please enter the number over 100: "))
num2 = int(input("Please enter the number under 10: "))

print(f"{num2} goes into {num1}: {num1 // num2} times")
