"""
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines.
"""

people = {}

for _ in range(4):
	name = input("Please enter your name: ")
	age = int(input("Please enter your age: "))
	shoe_size = int(input("Please enter your shoe size: "))
	print()
	
	people[name] = {'age': age, 'shoe_size': shoe_size}

name = input("Please enter a name: ")

del people[name]

for name, data in people.items():
	print(f"{name} is {data['age']} y.o. and has {data['shoe_size']} shoe size")
