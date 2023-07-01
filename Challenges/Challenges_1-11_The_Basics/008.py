"""
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.
"""

bill_price = int(input("Please enter the total price of the bill: "))
people_count = int(input("How many people are there? Please enter here: "))

print(f"Each person must pay {round(bill_price / people_count)}")
