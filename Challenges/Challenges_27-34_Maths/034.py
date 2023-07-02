"""
Display the following message:
1) Square
2) Triangle

Enter a number:
If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.
"""

print("1) Square", "2) Triangle", '', sep='\n')

num = int(input("Enter a number: "))

if num == 1:
	side_len = int(input("Please enter the length of side: "))
	
	print(f"The area is {side_len ** 2}")
elif num == 2:
	base = int(input("Please enter the base: "))
	height = int(input("Please enter the height: "))
	
	print(f"The area is {(base * height) / 2}")
else:
	print("Incorrect option")
