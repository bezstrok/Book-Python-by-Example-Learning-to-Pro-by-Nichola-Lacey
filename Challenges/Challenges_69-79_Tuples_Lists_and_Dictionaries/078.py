"""
Create a list containing the titles of
four TV programmes and display
them on separate lines. Ask the
user to enter another show and a
position they want it inserted into
the list. Display the list again,
showing all five TV programmes in
their new positions.
"""

tvs = ['ESPN', 'HBO', 'Discovery Channel', 'NBC']

print(*tvs, sep='\n')

channel = input("Please enter another channel: ")
index = int(input("What positition you want to insert into?\n"))

tvs.insert(index, channel)

print(*tvs, sep='\n')
