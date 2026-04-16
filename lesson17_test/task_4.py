"""
Task 4
Напишите программу которая умеет добавлять единицу к числу и возращает список,
не конвентируя в строку/число. Число хранится в виде списка.
Например число 123 будет храниться в виде списка: [1, 2, 3].
В результате прибавления единицы должен получиться список: [1, 2, 4].
[9] => [1,0]
[1,2,31 => [1,2,4]
[1,1,9] → [1,2,0]
[9,9,91=>11,0,0,0
"""


def number_count(list_number):
    for item in range(len(list_number) - 1, -1, -1):
        if list_number[item] < 9:
            list_number[item] += 1
            return list_number
        list_number[item] = 0
    return list_number[item] + item


print(number_count([1, 1, 9]))
