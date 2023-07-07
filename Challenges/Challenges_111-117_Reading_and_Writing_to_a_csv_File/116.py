"""
Import the data from the Books.csv file into a list. Display the
list to the user. Ask them to select which row from the list
they want to delete and remove it from the list. Ask the user
which data they want to change and allow them to change it.
Write the data back to the original .csv file, overwriting the
existing data with the amended data.
"""

import csv

with open("Books.csv", 'r') as f:
	reader = csv.reader(f)
	header = next(reader)
	data = list(reader)

print("Row Number", *header, sep=' | ')
for i, row in enumerate(data):
	print(i, *row, sep=' | ')

num = int(input("Please enter a row number you want to delete: "))
del data[num]

print("Row Number", *header, sep=' | ')
for i, row in enumerate(data):
	print(i, *row, sep=' | ')

num = int(input("Please enter a row number you want to change: "))
row = data[num]
print(' | '.join(f"{i}: {part}" for i, part in enumerate(row)))

num = int(input("Please enter which part you want to change: "))
el = input("Please enter a new value: ")

row[num] = el

with open("Books.csv", 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerows(data)
