"""
Display an array of five
numbers. Ask the user to
select one of the numbers.
Once they have selected a
number, display the
position of that item in the
array. If they enter
something that is not in
the array, ask them to try
again until they select a
relevant item.
"""

from array import array
from random import randint

arr = array('i', [randint(1, 99) for _ in range(5)])
print(*arr, sep='|')

while True:
	num = int(input("Please enter one of the numbers: "))
	if num in arr:
		print(arr.index(num))
		break
	else:
		print("The number is not in array!\nTry again")
