"""
Using the Books.csv file, display the data in
the file along with the row number of each.
"""

import csv

with open("Books.csv", 'r') as f:
	reader = csv.reader(f)
	print("Row Number", *next(reader), sep=' | ')
	for i, data in enumerate(reader, 1):
		print(i, *data, sep=' | ')
