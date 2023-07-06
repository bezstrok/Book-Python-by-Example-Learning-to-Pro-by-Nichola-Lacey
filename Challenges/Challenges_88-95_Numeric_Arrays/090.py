"""
Ask the user to enter numbers. If they enter a
number between 10 and 20, save it in the array,
otherwise display the message “Outside the
range”. Once five numbers have been
successfully added, display the message “Thank
you” and display the array with each item shown
on a separate line.
"""

from array import array

arr = array('i')

cnt = 0
print("Please enter numbers")
while True:
	num = int(input())
	if 10 <= num <= 20:
		arr.append(num)
		cnt += 1
	else:
		print("Outside the range")
	if cnt >= 5: break

print("Thank you")
print(*arr, sep='\n')
