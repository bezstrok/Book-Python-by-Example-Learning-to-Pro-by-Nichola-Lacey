"""
Using the 2D list from program 096, ask the user
which row they would like displayed and display
just that row. Ask them to enter a new value and
add it to the end of the row and display the row
again.
"""

lst = [[2, 5, 8],
       [3, 7, 4],
       [1, 6, 9],
       [4, 2, 0]]

index = int(input("Which row do you want to display?: "))
row = lst[index]

print(row)
value = int(input("Please enter a new value: "))
row.append(value)

print(row)
