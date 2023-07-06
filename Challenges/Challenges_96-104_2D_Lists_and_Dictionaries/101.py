"""
Using program 100, ask the user for a name and a region. Display the relevant data. Ask
the user for the name and region of data they want to change and allow them to make
the alteration to the sales figure. Display the sales for all regions for the name they
choose.
"""

from pprint import pprint

rows = ('N', 'S', 'E', 'W')

lst = {'John': (3056, 8463, 8441, 2694),
       'Tom': (4832, 6786, 4737, 3612),
       'Anne': (5239, 4802, 5820, 1859),
       'Fiona': (3904, 3645, 8821, 2451)}

for key, value in lst.items():
	lst[key] = dict(zip(rows, value))

pprint(lst)

name = input("Please enter a name: ")
region = input("Please enter a region: ")

data = int(input("Please enter a value: "))

lst[name][region] = data

pprint(lst[name])
