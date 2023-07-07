"""
Using the Books.csv file
from program 111, ask
the user to enter another
record and add it to the
end of the file. Display
each row of the .csv file
on a separate line.
"""

import csv

book = input("Please enter a book: ")
author = input("Please enter an author: ")
year = int(input("Please enter a year released: "))

with open("Books.csv", 'a', newline='') as f:
	writer = csv.writer(f)
	writer.writerow((book, author, year))

with open("Books.csv", 'r') as f:
	reader = csv.reader(f)
	for data in reader:
		print(*data, sep=' | ')
