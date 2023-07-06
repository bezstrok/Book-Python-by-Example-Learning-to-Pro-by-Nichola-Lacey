"""
Create the following using a 2D dictionary showing
the sales each person has made in the different
geographical regions:
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
