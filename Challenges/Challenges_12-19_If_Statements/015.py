"""
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
"""

MY_COLOR = "red"

color = input("Please enter your favourite color: ").lower()

if color == MY_COLOR:
	print(f"I like {color} too")
else:
	print(f"I don't like {color}, I prefer {MY_COLOR}")
