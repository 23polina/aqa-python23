"""
Task 1: Files
Напишите программу, которая создает текстовый файл(если его нету) "students.txt".
Запишите в файл список студентов, номер группы, их оценки.
Каждый студент на новой строке.
Откройте файл и прочитайте всю информацию из него.
Напечатайте общее количество студентов,
количество студентов для каждой группы и
среднюю оценку для каждой группы.
Допишите эту информацию в конец файла
"""
import os

FILE_NAME = "students.txt"


def create_and_write_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            students = [
                "Ivanov I.I;Group# 101;1, 10, 8",
                "Petrov I.I;Group# 101;7, 2, 8",
                "Sidorov I.I;Group# 102;7, 8, 8",
                "Alishevich I.I;Group# 102;6, 9, 10"
            ]
            for student in students:
                file.write(student + "\n")
        print("File was created")


def read_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File Not Found")
        return []


def process_data(lines):
    total_students = 0
    groups = {}

    for line in lines:
        name, group, grades_str = line.strip().split(";")
        grades = list(map(int, grades_str.split(",")))
        total_students += 1
        if group not in groups:
            groups[group] = {
                "count": 0,
                "grades_sum": 0,
                "grades_count": 0
            }
        groups[group]["count"] += 1
        groups[group]["grades_sum"] += sum(grades)
        groups[group]["grades_count"] += len(grades)
        print(f"Processing student: {name}")
    return total_students, groups


def calculate_averages(groups):
    averages = {}
    for group, data in groups.items():
        if data["grades_count"] > 0:
            avg = data["grades_sum"] / data["grades_count"]
            averages[group] = round(avg, 2)
        else:
            averages[group] = 0
    return averages


def append_results(total_students, groups, averages):
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"Total Student amount is: {total_students}\n")

            for group in groups:
                file.write(
                    f"{group}: "
                    f"{groups[group]['count']} students, "
                    f"Average mark is {averages[group]}\n"
                )

        print("Data has been added into the file")
    except IOError as e:
        print(f"Error during adding datat into the file: {e}")


def main():
    create_and_write_file()
    lines = read_file()
    total_students, groups = process_data(lines)
    averages = calculate_averages(groups)
    append_results(total_students, groups, averages)


if __name__ == "__main__":
    main()
