"""
Ask the user for a list of five
integers. Store them in an array.
Sort the list and display it in
reverse order.
"""

from array import array

arr = array('i')

print("Please enter five numbers:")
for _ in range(5):
	num = int(input())
	arr.append(num)

print(sorted(arr, reverse=True))
