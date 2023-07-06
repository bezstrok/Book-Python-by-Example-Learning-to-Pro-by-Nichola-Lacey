"""
Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line).
"""

from array import array
from random import randint

arr = array('i', [randint(1, 999) for _ in range(5)])

print(*arr, sep='\n')
