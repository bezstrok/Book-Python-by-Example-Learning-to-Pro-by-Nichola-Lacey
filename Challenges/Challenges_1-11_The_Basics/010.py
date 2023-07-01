"""
There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.
"""

POUND = 2.204

kilograms = int(input("Please enter the weight in kilograms: "))

print(f"The weight in pounds is {round(kilograms * POUND, 2)}")
