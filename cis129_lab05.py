# Lab 5 The Bottle Return Program
# Robert Zuchowski
# 2024-10-06
# tracks the number of returned bottles and calculate payout

# variables used for all iterations
days_in_week = 7
payout_per_bottle = 0.10
keep_going = 'y'

# loop at least one time to collect one week of data
while keep_going == 'y':
    # initialize variables for each iteration of a week
    today_bottles = 0
    total_bottles = 0
    total_payout = 0
    counter = 1

    # repeat prompt for each of 7 days in a week
    while counter <= days_in_week:
        today_bottles = input(f"Enter number of bottles for day #{counter}: ")

        # code to set value of variable totalBottles 
        total_bottles += int(today_bottles)
        # increment counter
        counter += 1

    # code to set value of variable totalPayout
    total_payout = total_bottles * payout_per_bottle
    # code to print the number of total bottles and total payout
    print(f"The total number of bottles collected is {total_bottles}")
    print(f"The total paid out is ${total_payout:.1f}")

    # prompt to enter another week of data
    print("Do you want to enter another week's worth of data?")
    keep_going = input("(Enter y or n): ")
    # repeat prompt until input is valid
    while keep_going != 'y' and keep_going != 'n':
        keep_going = input("(Enter y or n): ")