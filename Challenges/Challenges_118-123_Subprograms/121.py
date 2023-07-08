"""
Create a program that will allow the user to easily manage a list of names. You should
display a menu that will allow them to add a name to the list, change a name in the
list, delete a name from the list or view all the names in the list. There should also be a
menu option to allow the user to end the program. If they select an option that is not
relevant, then it should display a suitable message. After they have made a selection
to either add a name, change a name, delete a name or view all the names, they
should see the menu again without having to restart the program. The program
should be made as easy to use as possible.
"""


def add():
	value = input("Please enter a new name: ")
	lst.append(value)


def change():
	display()
	id = int(input("Please enter the index of value you want to change: "))
	value = input("Please enter a new name: ")
	
	lst[id] = value


def delete():
	display()
	id = int(input("Please enter the index of value you want to delete: "))
	
	del lst[id]


def display():
	print(lst)


def end():
	print("Thank you for using this program!")
	exit()


def error():
	print("Invalid operation")


def display_menu():
	for i, name in options.items():
		print(f"{i}) {name.__name__}")
	
	print()
	option = int(input("Please choose the one of the following option: "))
	return options.get(option, error)


def main():
	global options, lst
	options = {1: add, 2: change, 3: delete, 4: display, 5: end}
	lst = []
	
	while True:
		display_menu()()


if __name__ == '__main__':
	main()
