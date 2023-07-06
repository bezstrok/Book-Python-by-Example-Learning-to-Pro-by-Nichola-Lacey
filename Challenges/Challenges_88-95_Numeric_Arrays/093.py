"""
Ask the user to enter five
numbers. Sort them into order
and present them to the user.
Ask them to select one of the
numbers. Remove it from the
original array and save it in a
new array.
"""

from array import array

arr = array('i')

print("Please enter five numbers:")
for _ in range(5):
	arr.append(int(input()))

arr = array('i', sorted(arr))

print(*arr, sep='|')
num = int(input("Please enter one of the numbers: "))

arr.remove(num)
new_arr = array('i', [num])

print(*arr, sep='|')
print(*new_arr, sep='|')
