"""
Create a .csv file that will store the following data. Call it “Books.csv”.
"""

import csv

header = ("Book", "Author", "Year Released")
data = (("To Kill A Mockingbird", "Harper Lee", 1960),
        ("A Brief History of Time", "Stephen Hawking", 1988),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1922),
        ("The Man Who Mistook His Wife for a Hat", "Oliver Sacks", 1985),
        ("Pride and Prejudice", "Jane Austen", 1813))

with open("Books.csv", 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerows(data)
