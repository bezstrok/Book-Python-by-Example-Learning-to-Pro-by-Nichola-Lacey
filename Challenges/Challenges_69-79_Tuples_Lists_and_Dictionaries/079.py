"""
Create an empty list called “nums”.
Ask the user to enter numbers.
After each number is entered, add
it to the end of the nums list and
display the list. Once they have
entered three numbers, ask them if
they still want the last number they
entered saved. If they say “no”,
remove the last item from the list.
Display the list of numbers.
"""

nums = []

count = 1
print("Please enter numbers:")
while True:
	nums.append(int(input(f"{count}. ")))
	count += 1
	
	if count > 3:
		answer = input("Do you want to continue?(yes\\no)\n")
		if answer == 'no':
			break

print(*nums, sep='\n')
