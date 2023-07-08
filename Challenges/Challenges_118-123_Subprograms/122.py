"""
Create the following menu:
If the user selects 1, allow them to add to a file
called Salaries.csv which will store their name
and salary. If they select 2 it should display all
records in the Salaries.csv file. If they select 3 it
should stop the program. If they select an
incorrect option they should see an error
message. They should keep returning to the
menu until they select option 3.
"""

import csv


def new_record():
	name = input("Please enter a name: ")
	salary = input("Please enter a salary: ")
	
	with open("Salaries.csv", 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow((name, salary))


def display():
	with open("Salaries.csv", 'r') as f:
		reader = csv.reader(f)
		for data in reader:
			print(*data, sep=' | ')


def end():
	print("Thank you for using this programm")
	exit()


def error():
	print("Invalid operation")


def display_menu(menu: dict):
	for i, name in menu.items():
		print(f"{i}) {name.__name__}")
	
	print()
	option = int(input("Please choose the one of the following option: "))
	return menu.get(option, error)


def main():
	options = {1: new_record, 2: display, 3: end}
	
	while True:
		display_menu(options)()


if __name__ == "__main__":
	main()
