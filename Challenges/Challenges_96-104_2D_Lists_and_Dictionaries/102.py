"""
Ask the user to enter the name, age and shoe size for four
people. Ask for the name of one of the people in the list and
display their age and shoe size.
"""

from pprint import pprint

people = {}

for _ in range(4):
	name = input("Please enter your name: ")
	age = int(input("Please enter your age: "))
	shoe_size = int(input("Please enter your shoe size: "))
	print()
	
	people[name] = {'age': age, 'shoe_size': shoe_size}

pprint(people)
name = input("Please enter a name of the people: ")
data = people[name]
print(f"{name} is {data['age']} y.o., shoe size is {data['shoe_size']}")
