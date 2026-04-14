"""
Task 1 оздайте XML файл, содержащий информацию о товарах в магазине (название, цена, количество).
Напишите программу, которая считывает данные из файла и
выводит общую стоимость всех товаров.
"""

import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)

tree = ET.parse('products.xml')
root = tree.getroot()


def count_price(file_root=root):
    total_price = 0
    for product in file_root.findall('product'):
        price = float(product.find('price').text)
        total_price += price
    return total_price


counted_price = count_price()
logging.info("Your total price is %s", counted_price)
