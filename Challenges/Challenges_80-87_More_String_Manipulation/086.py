"""
Ask the user to enter a new password. Ask
them to enter it again. If the two passwords
match, display “Thank you”. If the letters are
correct but in the wrong case, display the
message “They must be in the same case”,
otherwise display the message “Incorrect”.
"""

password = input("Please enter a new password: ").strip()
confirm = input("Please enter the same password again: ").strip()

if password == confirm:
	print("Thank you")
elif password.lower() == confirm.lower():
	print("They must be the same case")
else:
	print("Incorrect")
