"""
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.
"""

sports = ['Football', 'Basketball']

sport = input("Please enter a new sport: ").title()

sports.append(sport)
sports.sort()

print(*sports, sep='\n')
