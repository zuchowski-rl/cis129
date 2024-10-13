# Lab 6 Hotdog Cookout
# Robert Zuchowski
# 2024-10-13
# calculates bun and hotdog packages required for a number of hotdogs

import math


def get_total_hotdogs():
    """collects input from user to determine the total hotdogs required"""

    # repeat prompts until input is valid
    while True:
        try:
            attendees = int(input("Enter the maximum number of attendees: "))
            # only allow 0 or greater input values
            if attendees >= 0:
                break
            else:
                print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            hotdogs = int(input("Enter the number of hotdogs per attendee: "))
            if hotdogs >= 0:
                break
            else:
                print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return attendees * hotdogs


def show_results(total_hotdogs):
    """calculate and display the count of bun and hotdog packages required"""

    # constants
    DOGS = 10
    BUNS = 8

    # calculate hotdog packages using formula from lab instructions
    dogs_left = (DOGS - total_hotdogs % DOGS) % DOGS
    min_dogs = (total_hotdogs // DOGS) + (0 ** (0 ** dogs_left))

    # calcualate bun packages using the math module
    min_buns = math.ceil(total_hotdogs / BUNS)
    buns_left = min_buns * BUNS - total_hotdogs

    # display results
    print("Minimum packages of hot dogs needed:", min_dogs)
    print("Minimum packages of hot dog buns needed:", min_buns)
    print("Hot dogs remaining:", dogs_left)
    print("Hot dog buns remaining:", buns_left)


def main():
    show_results(get_total_hotdogs()) 


if __name__ == "__main__":
    main()
