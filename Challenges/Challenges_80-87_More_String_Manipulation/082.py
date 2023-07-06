"""
Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.
"""

poem = "The text from my favourite poem"
print(poem)

start = int(input("Please enter a start point: "))
end = int(input("Please enter an end point: "))

print(poem[start:end])
