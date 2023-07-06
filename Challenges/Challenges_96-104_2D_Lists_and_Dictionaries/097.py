"""
Using the 2D list from program 096, ask the user to
select a row and a column and display that value.
"""

from pprint import pprint

lst = [[2, 5, 8],
       [3, 7, 4],
       [1, 6, 9],
       [4, 2, 0]]

pprint(lst)

print("Please enter")
row = int(input("Row: "))
col = int(input("Col: "))

print(lst[row][col])
