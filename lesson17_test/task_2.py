"""
Task2:
Напишите 2 функции:
Которая запрашивает у пользователя число и выводит его квадрат
Которая запрашивает у пользователя число и определяет,
является ли оно четным или
нечетным
"""


def count_value():
    user_value = float(input("Enter a number "))
    return user_value ** 2


print(count_value())


def check_even_odd():
    user_value = int(input("Enter a number "))
    if user_value % 2 == 0:
        return "Your number is even"
    else:
        return "Your number is odd"


print(check_even_odd())
