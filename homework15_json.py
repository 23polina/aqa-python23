"""
Создайте JSON файл, содержащий информацию о футбольных клубах (название, страна, количество побед).
Напишите программу, которая считывает данные из файла
и выводит на экран информацию о клубе с наибольшим количеством побед.
"""
import json
import logging

logging.basicConfig(level=logging.INFO)

with open('football_clubs.json', 'r') as file:
    data = json.load(file)


def get_wins(club):
    return club['wins']


best_club = max(data['clubs'], key=get_wins)
logging.info("Your best club is %s %s wins, %s", best_club['name'], best_club['wins'], best_club['country'])

