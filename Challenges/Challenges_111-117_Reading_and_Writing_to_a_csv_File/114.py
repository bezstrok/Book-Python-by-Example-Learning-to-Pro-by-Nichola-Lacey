"""
Using the Books.csv file, ask the user
to enter a starting year and an end
year. Display all books released
between those two years.
"""

import csv

start = int(input("Please enter a start year: "))
end = int(input("Please enter an end year: "))

with open("Books.csv", 'r') as f:
	reader = csv.reader(f)
	next(reader)
	data = [data for data in reader if start <= int(data[2]) <= end]

for row in data:
	print(*row, sep=' | ')
