"""
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.
"""

subjects = ['Math', 'Biology', 'Geography', 'English', 'Physical Education', 'Physics']

print(*subjects, sep='\n')
sub = input("Please enter the subject you don't like: ").title()

subjects.remove(sub)

print()
print(*subjects, sep='\n')
