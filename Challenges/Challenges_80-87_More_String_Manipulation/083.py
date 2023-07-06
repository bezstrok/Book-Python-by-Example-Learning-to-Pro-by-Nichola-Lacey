"""
Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in
uppercase.
"""

flag = True
while flag:
	text = input("Please enter a word in uppercase: ")
	flag = not text.isupper()
