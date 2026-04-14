"""
Создайте YAML файл, содержащий информацию о книгах (название, автор, год выпуска).
Напишите программу, которая считывает данные из файла и
позволяет пользователю добавлять новые книги в файл.
"""

import yaml
import logging
from pprint import pprint

logging.basicConfig(level=logging.INFO)

with open('books.yaml') as f:
    books_data = yaml.safe_load(f)


def add_new_book(data=books_data):
    new_book = [
        {"title": "New Test title", "author": "Test Author", "year": 2026},
        {"title": "Title", "author": "Author", "year": 2024}
    ]

    data['books'].append(new_book)
    return data['books']


logging.info("New Books added %s", add_new_book())
