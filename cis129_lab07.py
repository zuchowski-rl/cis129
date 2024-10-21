# Module 7 Lab
# Robert Zuchowski
# 2024-10-20
# theatre seating sales calculator

# constant for section configuration
# list of tuples (section, seats, price)
SECTIONS = [
    ('A', 300, 20),
    ('B', 500, 15),
    ('C', 200, 10)
]


def main():

    display_welcome()
    
    # variables for output
    subtotal = 0
    tickets_total = 0
    output = "\n"

    for section, seats, price in SECTIONS:
        # get input from user
        tickets = get_tickets_sold(section, seats)

        # calculate and update output variables
        section_total = tickets * price
        subtotal += section_total
        tickets_total += tickets

        # add section data to output
        output += f"Section {section} Tickets: {tickets:>5} @ ${price:.2f}" 
        output += f" ${section_total:10.2f}\n"

        # display running subtotal
        print(f"Section Total   : ${section_total:10.2f}")
        print(f"Running Subtotal: ${subtotal:10.2f}")

    # add final totals to output
    output += f"Total Tickets    : {tickets_total:>5} \n"
    output += f"Grand total...................... ${subtotal:10.2f}"

    # display output
    print(output)


def display_welcome():
    print("Welcome...")
    for section, seats, price in SECTIONS:
        print(f"Section {section}: {seats} seats available at ${price:.2f} each.")


def get_tickets_sold(section, seats):
    print()
    tickets_sold = input(f"Enter tickets sold for section {section}: ")

    while is_invalid(tickets_sold, seats):
        print(f"Invalid input. Enter a number between 0 and {seats}.")
        tickets_sold = input(f"Enter tickets sold for section {section}: ")

    return int(tickets_sold)


def is_invalid(value, seat_limit):
    # test that input is an integer
    try:
        value = int(value)
    except ValueError:
        return True
    # test that input is positive
    if value < 0:
        return True
    # test that input does not exceed seat limit
    if value > seat_limit:
        return True
    
    return False


if __name__ == "__main__":
    main()