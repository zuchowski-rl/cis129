# Author: Robert Zuchowski
# Module 3 Lab - Coffee shop simulator
# Takes a customer's order and prints a reciept

# price variables
tax_rate = 0.06
coffee_price = 5
muffin_price = 4
tea_price = 2
scone_price = 3

# get item quantities with the input function
print("***************************************")
print("My Coffee and Muffin Shop")
coffees_bought = int(input("Number of coffees bought?\n"))
muffins_bought = int(input("Number of muffins bought?\n"))
teas_bought = int(input("Number of teas bought?\n"))
scones_bought = int(input("Number of scones bought?\n"))
print("***************************************\n")

# calculate totals
coffee_total = coffees_bought * coffee_price
muffin_total = muffins_bought * muffin_price
tea_total = teas_bought * tea_price
scone_total = scones_bought * scone_price
sub_total = muffin_total + coffee_total + scone_total + tea_total
tax_total = sub_total * tax_rate
grand_total = sub_total + tax_total

# print the reciept
print("***************************************")
print("My Coffee and Muffin Shop Reciept")
print(f"{coffees_bought} Coffee at ${coffee_price} each: $ {coffee_total:,.2f}")
print(f"{muffins_bought} Muffins at ${muffin_price} each: $ {muffin_total:,.2f}")
print(f"{teas_bought} Tea at ${tea_price} each: $ {tea_total:,.2f}")
print(f"{scones_bought} Scones at ${scone_price} each: $ {scone_total:,.2f}")
print(f"6% tax: $ {tax_total:,.2f}")
print("---------")
print(f"Total: $ {grand_total:,.2f}")
print("Thank you for visting My Coffee and Muffin Shop!")
print("***************************************")