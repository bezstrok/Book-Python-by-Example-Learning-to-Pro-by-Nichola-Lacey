"""
Ask the user to type in their name
and then tell them how many vowels
are in their name.
"""

vowels = set("aeuio")

name = input("Please enter your name: ")

count = sum(i in vowels for i in name.lower())
print(f"There are {count} vowels in your name")
