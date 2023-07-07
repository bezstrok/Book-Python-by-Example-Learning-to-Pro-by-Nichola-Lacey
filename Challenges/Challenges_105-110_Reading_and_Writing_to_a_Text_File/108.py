"""
Open the Names.txt file. Ask the user to input a
new name. Add this to the end of the file and
display the entire file.
"""

name = input("Please enter a new name: ")

with open("Names.txt", 'a') as f:
	f.write(name)
