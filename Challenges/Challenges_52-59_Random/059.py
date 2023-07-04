"""
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.
"""

import random

witty = ("I bet you are {} with envy", "You are probably feeling {} right now")
colors = ['blue', 'green', 'orange', 'white', 'black']

answer = random.choice(colors)

print("You need to guess the one of colors:")
for i, color in enumerate(colors, 1):
	print(f"{i}. {color.capitalize()}")
print()
guess = input("Enter a color: ").lower()

if guess == answer:
	print("Well done")
else:
	while guess != answer:
		print(random.choice(witty).format(answer.upper()))
		guess = input("Enter a color: ").lower()
	print("Correctly!")
