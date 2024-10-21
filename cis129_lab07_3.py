# Module 7 assignment Lab 7-3
# Robert Zuchowski
# 2024-10-19
# The Dice Game

# add libraries needed
import random

def main():
    print()
    # initialize variables
    end_program = 'no'
    player_one, player_two = input_names()
    # while loop to run program again
    while end_program == 'no':

        # call to roll_dice
        winner_name = roll_dice(player_one, player_two)

        # call to display_info
        display_info(winner_name)

        end_program = input('Do you want to end program? (yes/no): ').lower()
        # there are only two valid answers after adjusting for case
        while end_program not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            end_program = input('Do you want to end program? (yes/no): ')

# this function gets the players names
def input_names():

    player_one = input("Enter name for player 1: ")
    # test for empty input
    while len(player_one) < 1:
        print("Invalid input.")
        player_one = input("Enter name for player 1: ")

    player_two = input("Enter name for player 2: ")
    while len(player_two) < 1:
        print("Invalid input.")
        player_two = input("Enter name for player 2: ")

    return player_one, player_two

# this function will get the random values
def roll_dice(player_one, player_two):

    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    print(f"{player_one} rolled {p1number}")
    print(f"{player_two} rolled {p2number}")

    if p1number == p2number:
        winner_name = "TIE"
    elif p1number > p2number:
        winner_name = player_one
    else:
        winner_name = player_two

    return winner_name

# this function displays the winner
def display_info(winner_name):
    print(f"The winner is: {winner_name}!")

main()