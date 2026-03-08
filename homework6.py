# Task 1 - Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
line1 = 'www.my_site.com#about'
print(line1.replace("#","/"))

# Task 2 - Напишите программу, которая добавляет ‘ing’ к словам
word = 'apple'
print(word.__add__("ing"))

# Task 3 - В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
line2 = 'Ivanou Ivan'
l2 = line2.split()
switched_line = " ".join(l2[:: -1])
print(switched_line)

# Task 4 - Напишите программу которая удаляет пробел в начале, в конце строки
line3 = input("Enter a string ")
left_result = line3.lstrip()
print(left_result.rstrip())

line4 = "       Long string        "
left_result_2 = line4.lstrip()
print(left_result_2.rstrip())

# Task 5 - Исправьте данное имя - "pARiS" >> "Paris"
name = 'pARiS'
print(name.capitalize())

# Task 6 - Перевести строку в список "Robin Singh" => ["Robin”, “Singh"],
# "I love arrays they are my favorite" => [
# "I", "love", "arrays", "they", "are", "my", "favorite"]
line5 = "Robin Singh"
converted_string = line5.split()
print(converted_string)

line6 = "I love arrays they are my favorite"
converted_string2 = line6.split()
print(converted_string2)

# Task 7 - Дан список: [Robin Singh], и 2 строки: "Welcome" и "airport".
# Напечатайте текст: “Hello, Robin Singh! Welcome to airport”
my_list = ['Robin Singh']
list_into_str = " ".join(my_list)
str_1 = 'Welcome'
str_2 = "airport"
print(f"Hello, {list_into_str}! {str_1} to {str_2}")

# Task 8 - Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
my_list2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
list_into_str2 = " ".join(my_list2)
print(list_into_str2)

# Task 9 - Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
my_array = ["apple", "orange", "cat", "dog", "traveling", "QA", "gym", "health", "IT", "aviation"]
my_array.insert(2, "cat23")
del my_array[5]
print(my_array)
