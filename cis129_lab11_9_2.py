# Module 11 Lab Exercise 9.2
# Robert Zuchowski
# 2024-11-17
# Class average program adapted from fig03_02.py


def read_grades(file_path: str = 'grades.txt') -> None:
    """read and display grade info from file"""

    total = 0 # sum of grades 
    grade_counter = 0 # number of grades entered

    try:
        # open file for reading
        with open(file_path, 'r') as grades:
            print("Grades entered:")
            for grade in grades:
                grade = grade.strip()
                # skip empty rows
                if grade:
                    try:
                        total += float(grade)
                    except ValueError:
                        print(f'Exiting. File contains invalid data: "{grade}"')
                        exit()
                    else:
                        grade_counter += 1
                        print(grade)
    except FileNotFoundError:
        print(f'File {file_path} does not exist. Validate file name is correct.')
        exit()

    # termination phase
    if grade_counter != 0:
        average = total / grade_counter
        print(f'{grade_counter} grades collected.')
        print(f'Average grade is {average:.2f}')
    else:
        print('No grades were entered.')


if __name__ == "__main__":
    read_grades()