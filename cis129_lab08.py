# Module 8 Lab
# Robert Zuchowski
# 2024-10-27
# palindrome tester

import string

def is_palindrome(input_string : str) -> bool:
    """tests if string contains a palindrome, ignores spaces and punctuation"""
    # ignore case by doing comparison in lowercase
    input_string = input_string.lower()

    # emulate stack with list
    stack = []

    for character in input_string:
        # discard spaces and punctuation
        if character not in string.punctuation and not character.isspace():
            stack.append(character)

    for character in stack:
        # compare from outside in, return False on first mismatch
        if character != stack.pop():
            return False
        
    # return true after no mismatches 
    return True


def check_test_data() -> None:

    test_data = [
        "radar",
        "odd",
        "αββα",
        "even",
        "Madam, I'm Adam.",
        "a",
        "",
        1001,
        13,
        1.1,
        1.001,
        -1
    ]
    
    for item in test_data:
        display_string = f'"{str(item)}"'
        print(f"{display_string:<20}", is_palindrome(str(item)))


def check_user_input() -> None:

    sentinel = '#'
    prompt = f"Enter text to test if it is a palindrome, enter {sentinel} to exit: "

    input_string = input(prompt)
    
    while input_string.strip() != sentinel:
        # validate input contains alphanumeric text
        if len([c for c in input_string if c.isalnum()]) > 0:
            print(is_palindrome(input_string))
            input_string = input(prompt)
        else:
            input_string = input("Input must include letters or numbers. \n" \
                                 + prompt)


if __name__ == "__main__":
    check_test_data()
    check_user_input()
