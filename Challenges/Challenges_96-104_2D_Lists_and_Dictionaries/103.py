"""
Adapt program 102
to display the
names and ages of
all the people in
the list but do not
show their shoe
size.
"""

people = {}

for _ in range(4):
	name = input("Please enter your name: ")
	age = int(input("Please enter your age: "))
	shoe_size = int(input("Please enter your shoe size: "))
	print()
	
	people[name] = {'age': age, 'shoe_size': shoe_size}

for name, data in people.items():
	print(f"{name} | age is {data['age']}")
