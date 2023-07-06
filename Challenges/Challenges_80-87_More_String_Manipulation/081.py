"""
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
"""

subject = input("Please enter your favourite school subject: ")

print('-'.join(tuple(subject)) + '-')
