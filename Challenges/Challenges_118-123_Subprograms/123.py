"""
In Python, it is not technically possible to directly
delete a record from a .csv file. Instead you need
to save the file to a temporary list in Python,
make the changes to the list and then overwrite
the original file with the temporary list.
Change the previous program to allow you to do
this. Your menu should now look like this:
"""

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


def delete():
	with open("Salaries.csv", 'r') as f:
		reader = csv.reader(f)
		data = list(reader)
	
	for i, row in enumerate(data[1:], 1):
		print(i, *row, sep=' | ')
	
	num = int(input("Please enter the index of row you want to delete: "))
	del data[num]
	
	with open("Salaries.csv", 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(data)


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
	options = {1: new_record, 2: display, 3: delete, 4: end}
	
	while True:
		display_menu(options)()


if __name__ == "__main__":
	main()
