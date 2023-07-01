"""
Ask the user for their name and their age. Add 1 to their age
and display the output [Name] next birthday you
will be [new age].
"""

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(f"{name} next birthday you will be {age + 1}")
