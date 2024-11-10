# Module 10 Lab
# Robert Zuchowski
# 2024-11-08
# Exercise 8.1 Check Protection

def format_amount(amount: float, spaces: int=10) -> str:
    """format a currency amount for safe printing on a check"""
    return f"{amount:*>{spaces},.2f}"

def process_input() -> None:
    """takes user input and prints format_amount result"""

    while True:
        amount = input("Enter a currency amount: ")
        try:
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Invalid input. Amount must be greater than 0.")
        except ValueError:
            print("Invalid input. Amount must be a number.")

    print(format_amount(amount))

if __name__ == "__main__":
    process_input()