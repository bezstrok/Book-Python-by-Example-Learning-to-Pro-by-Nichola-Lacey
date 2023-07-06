"""
Enter a list of ten colours.
Ask the user for a starting
number between 0 and 4
and an end number
between 5 and 9. Display
the list for those colours
between the start and end
numbers the user input.
"""

colors = ['Blue', 'White', 'Orange', 'Black', 'Purple', 'Grey', 'Yellow', 'Red', 'Brown', 'Gold']

start = int(input("Please enter a start number from 0 and 4: "))
end = int(input("Please enter an end number from 5 and 9: "))

print(colors[start:end])
