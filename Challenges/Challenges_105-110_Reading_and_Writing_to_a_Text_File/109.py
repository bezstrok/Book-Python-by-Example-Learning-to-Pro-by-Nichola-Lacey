"""
Display the following menu to the user:
Ask the user to enter 1, 2 or 3. If they select
anything other than 1, 2 or 3 it should display a
suitable error message.
If they select 1, ask the user to enter a school
subject and save it to a new file called
“Subject.txt”. It should overwrite any existing file
with a new file.
If they select 2, display the contents of the
“Subject.txt” file.
If they select 3, ask the user to enter a new
subject and save it to the file and then display
the entire contents of the file.
Run the program several times to test the
options
"""

options = ("Create a new file", "Display the file", "Add a new item to the file")

for i, o in enumerate(options, 1):
	print(f"{i}) {o}")

num = int(input("Please enter the number of option: "))
if num == 1:
	subject = input("Please enter your favourite subject: ")
	with open("Subject.txt", 'w') as f:
		f.write(subject + '\n')
elif num == 2:
	with open("Subject.txt", 'r') as f:
		print(f.read())
elif num == 3:
	subject = input("Please enter your favourite subject: ")
	with open("Subject.txt", 'a') as f:
		f.write(subject + '\n')
	
	with open("Subject.txt", 'r') as f:
		print(f.read())
else:
	print("Invalid Operation")
