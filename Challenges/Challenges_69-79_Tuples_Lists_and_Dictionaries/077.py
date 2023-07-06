"""
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.
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
print()

name = input("Please enter a name from this list: ").title()
index = people.index(name)
print(f"The index of this name is {index}")

answer = input("Do you want to delete him? (yes\\no)\n").lower()
if answer == 'yes':
	del people[index]

print(*people, sep='\n')
