"""
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
"""

with open("Names.txt", 'w') as fout:
	for name in ('Sasha', 'Kirill', 'Stepan', 'Vasia', 'Roma'):
		fout.write(name + '\n')
