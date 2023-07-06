"""
Add to program 069 to ask the
user to enter a number and
display the country in that
position.
"""

countries = ("New Zealand", "Russia", "Netherlands", "France", "Poland")

print(*countries, sep='\n')

county = int(input("Please enter a number between 0 and 4: "))

print(f"The country is {countries[county]}")
