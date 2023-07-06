"""
Create an array which contains
five numbers (two of which
should be repeated). Display
the whole array to the user. Ask
the user to enter one of the
numbers from the array and
then display a message saying
how many times that number
appears in the list.
"""

from array import array

arr = array('i', (1, 4, 3, 4, 5))

print("The array:", *arr)

num = int(input("Please enter one of the numbers: "))
print(f"The number {num} appears {arr.count(num)} times")
