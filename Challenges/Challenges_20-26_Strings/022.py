"""
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
"""

name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")

full_name = (name + ' ' + surname).title()

print(full_name)
