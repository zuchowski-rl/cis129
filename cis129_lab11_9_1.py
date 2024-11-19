# Module 11 Lab Exercise 9.1
# Robert Zuchowski
# 2024-11-17
# Class average program adapted from fig03_02.py


def enter_grades(file_path: str = 'grades.txt') -> None:
    """prompt for and write input grades to file"""

    prompt = 'Enter grade, -1 to end: '

    # open file for writing
    with open(file_path, 'w') as output:
        grade = input(prompt).strip() # get one grade
        while grade != '-1':
            try:
                # validate grade
                grade = float(grade)
                if grade>= 0:
                    print(grade, file=output)
                else:
                    print("Invalid input. Enter a number 0 or greater.")
            except ValueError:
                print('Invalid Input. Enter a number 0 or greater.')

            grade = input(prompt).strip()


if __name__ == "__main__":
    enter_grades()