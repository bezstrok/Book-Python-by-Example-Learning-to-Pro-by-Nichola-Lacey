"""
Create a list of four three-digit
numbers. Display the list to the
user, showing each item from
the list on a separate line. Ask
the user to enter a three-digit
number. If the number they
have typed in matches one in
the list, display the position of
that number in the list,
otherwise display the message
“That is not in the list”.
"""

numbers = [123, 321, 213, 312]

print(*numbers, sep='\n')

num = int(input("Please enter a three-digit number: "))

if num in numbers:
	print(numbers.index(num))
else:
	print("That is not in the list")
