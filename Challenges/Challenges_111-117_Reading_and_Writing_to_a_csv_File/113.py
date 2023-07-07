"""
Using the Books.csv file, ask the user how many records
they want to add to the list and then allow them to add
that many. After all the data has been added, ask for an
author and display all the books in the list by that author.
If there are no books by that author in the list, display a
suitable message.
"""

import csv

num = int(input("Please enter how many books you want to add: "))

with open("Books.csv", 'a', newline='') as f:
	writer = csv.writer(f)
	
	for _ in range(num):
		book = input("Please enter a book: ")
		author = input("Please enter an author: ")
		year = int(input("Please enter a year released: "))
		writer.writerow((book, author, year))

author = input("Please enter an author name: ")

with open("Books.csv", 'r') as f:
	reader = csv.reader(f)
	next(reader)

	data = [data for data in reader if data[1] == author]

if data:
	for info in data:
		print(*info, sep=' | ')
else:
	print("There is no data")

