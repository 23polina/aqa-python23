"""
Task 1: Положительные аргументы функции
Напишите декоратор @validate_arguments, который проверяет,
что все аргументы функции являются положительными числами.
Если встречается аргумент, не соответствующий этому условию,
функция должна вывести сообщение об ошибке.

Task 2: Вернуть число
Создайте декоратор, который проверяет, является ли результат функции числом и
выводит сообщение об ошибке, если это не так.

Task 3: Декоратор типов
Напишите декоратор, который проверял бы тип параметров функции, конвертировал
их если надо и складывал

Task 4: Функция кэширования
Напишите декоратор @cache, который кэширует результаты вызова функции и
возвращает закэшированное значение при повторных вызовах с теми же аргументами.
"""


# Task 1:
def validate_arguments(func):
    def wrapper(*args):
        for items in args:
            if items < 0:
                raise ValueError("Negative number")
        return func(*args)

    return wrapper


@validate_arguments
def check_number(number):
    return number


print(check_number(5))

print(check_number(-5))


# Task 2:
def number_check(func):
    def wrapper(value):
        result = func(value)
        if not isinstance(result, (int, float)):
            raise ValueError("Functional result isn't number")
        print(result)
        return result

    return wrapper


@number_check
def check_value(value):
    return value


check_value("lalal")


# Task 3:
def typed(type_):
    def check_type(func):
        new_list = []

        def wrapper(*args):
            for items in args:
                if not isinstance(items, type_):
                    new_value = type_(items)
                    new_list.append(new_value)
                else:
                    new_list.append(items)
            return func(*new_list)

        return wrapper

    return check_type


@typed(type_=str)
def add(a, b):
    return a + b


print(add("5", 6))


@typed(type_=int)
def add_1(a, b):
    return a + b


print(add_1("5", 6))


# Task 4:
def cache(func):
    cached_values = {}

    def wrapper(key):
        if key in cached_values:
            return cached_values[key]
            # print(cached_values)
        results = func(key)
        cached_values[key] = results
        # print(cached_values)
        return results

    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
