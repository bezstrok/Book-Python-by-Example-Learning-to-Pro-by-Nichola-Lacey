"""
Create two arrays (one
containing three numbers that
the user enters and one
containing a set of five random
numbers). Join these two arrays
together into one large array.
Sort this large array and display
it so that each number appears
on a separate line.
"""

from array import array
from random import randint

arr_1 = array('i')
arr_2 = array('i', [randint(1, 999) for _ in range(5)])

print("Please enter three numbers:")
for _ in range(3):
	arr_1.append(int(input()))

arr_3 = array('i')
arr_3.extend((*arr_1, *arr_2))

print(*sorted(arr_3), sep='\n')
