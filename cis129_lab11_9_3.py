# Module 11 Lab Exercise 9.3
# Robert Zuchowski
# 2024-11-17
# data entry cli app for exam grades

import csv


def input_grades(file_path: str='grades.csv') -> None:
    """collect and write student exam grade info to csv file"""
    with open(file_path, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        # collect input
        data = enter_record()
        while data:
            # write output
            writer.writerow(data)
            data = enter_record()


def enter_record() -> list:
    """prompt for and build a student exam record"""
    firstname = input("Enter first name, -1 to stop entering records: ").strip()

    if firstname == '-1':
        return []
    else:
        lastname = input("Enter last name: ").strip()
        exam1 = get_grade("Enter Exam 1 grade: ")
        exam2 = get_grade("Enter Exam 2 grade: ")
        exam3 = get_grade("Enter Exam 3 grade: ")

        return [firstname, lastname, exam1, exam2, exam3]


def get_grade(prompt: str) -> float:
    """prompt for and validate grade input"""
    while True:
        data = input(prompt).strip()
        try:
            grade = float(data)
            if grade >= 0:
                return grade
            else:
                print('Invalid input. Enter a number 0 or greater.')
        except ValueError:
            print('Invalid input. Enter a number 0 or greater.')


if __name__ == "__main__":
    input_grades()