"""
Напишите функцию, преобразующую входную строку в выходную как в примерах,
 Пусть s = "abcdef...xуz", тогда вывод будет таким:
f(s, 2) = "abba"
"""


def convert_str(value, number):
    part_value = value[:number]
    new_value = part_value + part_value[:-1][::-1]
    print(new_value)


print(convert_str("abcdef", 2))
