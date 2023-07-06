"""
Change your previous program
to ask the user which row they
want displayed. Display that
row. Ask which column in that
row they want displayed and
display the value that is held
there. Ask the user if they want
to change the value. If they do,
ask for a new value and change
the data. Finally, display the
whole row again.
"""

lst = [[2, 5, 8],
       [3, 7, 4],
       [1, 6, 9],
       [4, 2, 0]]

row_index = int(input("Which row do you want to display?: "))
row = lst[row_index]
print(row)

col_index = int(input("Which column do you want to display?: "))
col = row[col_index]
print(col)

answer = input("Do you want to change this data? (y\\n)\n").lower()
if answer == 'y':
	row[col_index] = int(input("Please enter a new value: "))

print(row)
