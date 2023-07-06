"""
Ask the user to type in a word and then
display it backwards on separate lines. For
instance, if they type in “Hello” it should
display as shown below:
"""

word = input("Please enter a word: ")

print(*word[::-1], sep='\n')
