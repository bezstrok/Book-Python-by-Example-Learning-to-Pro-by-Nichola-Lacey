"""
Using the Names.txt file you
created earlier, display the list of
names in Python. Ask the user to
type in one of the names and then
save all the names except the one
they entered into a new file called
Names2.txt.
"""

with open("Names.txt", 'r') as f:
	lst = list(map(str.strip, f.readlines()))

print(*lst, sep='\n')

name = input("Please enter the name from the list: ")

lst.remove(name)

with open("Names2.txt", 'w') as f:
	f.writelines(name + '\n' for name in lst)
