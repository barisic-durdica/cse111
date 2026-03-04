"""
Author: Durdica Barisic

Purpose: Python program that gets a customer’s subtotal as input and gets the current day of the week from your computer’s operating system.
"""
from datetime import datetime

discount_rate = 0.1
tax_rate = 0.06
today = datetime.now()
day_of_the_week = today.weekday()
subtotal = 0
quantity = -1

while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: "))
        subtotal += quantity * price

print(f"Total order ${subtotal:.2f}")
discount = 0
if day_of_the_week == 2 or day_of_the_week == 3:
    if subtotal >= 50:
        discount = round(subtotal * discount_rate, 2)
        print(f"Discount ${discount:.2f}")
    else:
        short = 50 - subtotal
        print(f"You can get a discount by ordering ${short:.2f} more.")

subtotal -= discount
tax = round(subtotal * tax_rate, 2)
total = subtotal + tax
print(f"Tax ${tax:.2f}")
print(f"Total Due ${total:.2f}")
