"""
Task 6:
Реализуйте функцию которая умеет работать с файлами
(читать из заданного файла, записывать в заданный файл)
Программа считает количество строк, слов и букв в заданном файле
и дописывает эту информацию обратно в файл,
так же выводит эту информацию на экран.
"""

FILE_NAME = "students.txt"


def read_file():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        file_data = file.read()
        lines = len(file_data.splitlines())
        words = len(file_data.split())
        letters = len(file_data)
        return lines, words, letters


func_data = read_file()


def add_data_into_file(data):
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        lines, words, letters = data
        file_data = file.write(f"Your amount of lines - {lines}, "
                               f"words - {words} "
                               f"and letters {letters}")
        return file_data


def main():
    file = read_file()
    print("Strings:", file[0])
    print("Words:", file[1])
    print("Letters:", file[2])
    add_data_into_file(file)


main()
