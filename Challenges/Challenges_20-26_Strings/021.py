"""
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
"""

name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")

full_name = name + ' ' + surname

print(len(full_name))
