"""
Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party.
"""

name = input("Please enter a name: ")

print(f"{name} has now been invited")
count = 1

answer = input("Do you want to invite somebody else? (y\\n)\n")
while answer == 'y':
	name = input("Please enter a name: ")
	print(f"{name} has now been invited")
	count += 1
	answer = input("Do you want to invite somebody else? (y\\n)\n")

print(f"{count} people have coming to the party")
