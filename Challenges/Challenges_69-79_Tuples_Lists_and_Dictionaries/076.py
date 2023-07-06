"""
Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party.
"""

people = []

print("Please enter three names of people you want to invite to a party:")
for _ in range(3):
	people.append(input().title())

answer = input("Do you want to add another? (yes\\no)\n").lower()
while answer == 'yes':
	people.append(input("Please enter a name: ").title())
	answer = input("Do you want to add another? (yes\\no)\n").lower()

print(*people, sep='\n')
