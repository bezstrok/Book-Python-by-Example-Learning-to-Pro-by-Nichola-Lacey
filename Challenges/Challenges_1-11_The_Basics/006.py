"""
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a userfriendly format.
"""

started_value = int(input("How many slices of pizza did you start with?\n"))
end_value = int(input("How many slices of pizza have you eaten?\n"))

print(f"{started_value - end_value} slices of pizza have left!")
