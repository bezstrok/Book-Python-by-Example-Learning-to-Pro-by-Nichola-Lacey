"""
Create an array of five numbers
between 10 and 100 which each have
two decimal places. Ask the user to
enter a whole number between 2 and 5.
If they enter something outside of that
range, display a suitable error message
and ask them to try again until they
enter a valid amount. Divide each of the
numbers in the array by the number the
user entered and display the answers
shown to two decimal places.
"""

from array import array
from random import uniform

arr = array('f', [round(uniform(10, 100), 2) for _ in range(5)])

while True:
	num = float(input("Please enter a number between 2 and 5: "))
	
	if 2 <= num <= 5:
		for i in range(len(arr)):
			arr[i] = round(arr[i] / num, 2)
		break
	else:
		print("Outside the range!\nTry again")

print(*arr, sep='\n')
