"""
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.
"""

countries = ("New Zealand", "Russia", "Netherlands", "France", "Poland")

print(*countries, sep='\n')

county = input("Please enter a country: ").title()

print(f"The index of {county}: {countries.index(county)}")
