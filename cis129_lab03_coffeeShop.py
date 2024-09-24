# Author: Robert Zuchowski
# Module 3 Lab - Coffee shop simulator
# Takes a customer's order and prints a reciept

# price variables
tax_rate = 0.06
coffee_price = 5
muffin_price = 4

# get item quantities with the input function
print("***************************************")
print("My Coffee and Muffin Shop")
coffees_bought = int(input("Number of coffees bought?\n"))
muffins_bought = int(input("Number of muffins bought?\n"))
print("***************************************\n")

# calculate totals
coffee_total = coffees_bought * coffee_price
muffin_total = muffins_bought * muffin_price
sub_total = muffin_total + coffee_total
tax_total = sub_total * tax_rate
grand_total = sub_total + tax_total

# print the reciept
print("***************************************")
print("My Coffee and Muffin Shop Reciept")
print(f"{coffees_bought} Coffee at ${coffee_price} each: $ {coffee_total:,.2f}")
print(f"{muffins_bought} Muffins at ${muffin_price} each: $ {muffin_total:,.2f}")
print(f"6% tax: $ {tax_total:,.2f}")
print("---------")
print(f"Total: $ {grand_total:,.2f}")
print("***************************************")