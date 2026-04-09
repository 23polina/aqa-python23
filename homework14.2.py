"""
Task 2: Re
2.1
Напишите программу, которая будет считывать строки из текстового файла и
находить все даты в формате "dd.mm.yyyy".
Выведите найденные даты на экран.
2.2
Разработайте программу для проверки корректности паролей.
Пароль считается корректным, если он содержит не менее 8 символов,
включает хотя бы одну заглавную букву, одну строчную букву и одну цифру.
Task 3: Time
3.1
Создайте программу, которая будет запрашивать у пользователя две даты в формате "ГГГГ-ММ-ДД".
Вычислите и выведите на экран количество дней между этими датами.
3.2
Создайте программу, которая будет принимать ввод от пользователя в формате "ГГГГ-ММ-ДД" и проверять,
является ли введенная дата будущей или прошлой относительно текущей даты.
Выведите соответствующее сообщение на экран.
"""
import re


# Task 2.1
def found_value():
    with open('text_file_for_hw14.txt') as file:
        value = file.read()
        found_values = re.findall(r"\d{2}\.\d{2}\.\d{4}", value)
        print(found_values)


found_value()

# Task 2.2
user_password = input("Enter your password ")


def check_password(password=user_password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    if re.fullmatch(pattern, password):
        print("Your password is correct")
    else:
        print("Your password isn't according to standards")


check_password()

# Task 3.1
from datetime import datetime
from dateutil.relativedelta import relativedelta

first_date = input("Enter first date in YYYY-MM-DD format ")
second_date = input("Enter second date in YYYY-MM-DD format ")
formatted_first_date = datetime.strptime(first_date, "%Y-%m-%d")
formatted_second_date = datetime.strptime(second_date, "%Y-%m-%d")
if formatted_first_date > formatted_second_date:
    formatted_first_date, formatted_second_date = formatted_second_date, formatted_first_date
difference = relativedelta(formatted_second_date, formatted_first_date)
days_amount = (formatted_second_date - formatted_first_date).days
print(days_amount)

# Task 3.2
user_input = input("Enter date in YYYY-MM-DD format ")
user_date = datetime.strptime(user_input, "%Y-%m-%d")
today = datetime.today()
if user_date.date() > today.date():
    print("Your date in the future")
elif user_date.date() < today.date():
    print("Your date in the past")
else:
    print("You entered today's date")
