"""
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.
"""

people_num = int(input("Please enter a number of people: "))

if people_num < 10:
	for _ in range(people_num):
		name = input("Please enter name of participant\n")
		print(f"{name} has been invited")
else:
	print("Too many people")
