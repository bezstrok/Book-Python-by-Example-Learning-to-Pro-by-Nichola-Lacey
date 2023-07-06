"""
Ask the user to enter their
first name and then display
the length of their first name.
Then ask for their surname
and display the length of
their surname. Join their first
name and surname together
with a space between and
display the result. Finally,
display the length of their full
name (including the space).
"""

name = input("Please enter your first name: ")
print(len(name))

surname = input("Please enter your surname: ")
print(len(surname))

full_name = surname + ' ' + name
print(full_name, 'the len is ' + str(len(full_name)))
