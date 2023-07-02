"""
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).
"""

rhyme = input("Please enter a nursery rhyme: ")

print(f"The length of your nursery rhyme is {len(rhyme)}")

start = int(input("Please enter the starting number: "))
end = int(input("Please enter the ending number: "))

print(f"The section of selected nursery rhyme is\n{rhyme[start + 1:end + 1]}")
