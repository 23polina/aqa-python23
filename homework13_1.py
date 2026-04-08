"""
Task 1: Колода карт
Напишите программу которая содержит список карт,
умеет их перемешивать и позволяет пользователю достать карту из колоды по ее номеру.
Всего в колоде 54 карт. Класс Card содержит спискок номеров карт и список мастей.
"""

# Task1:
import random


class Card:
    number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    mast_list = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def return_cards(self):
        return f"{self.number} {self.mast}"


class CardDeck:
    def __init__(self):
        self.cards = self.create_desk()

    def create_desk(self):
        cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                cards.append(Card(number, mast))
        cards.append(Card("Jocker1", "Black"))
        cards.append(Card("Jocker2", "Red"))
        return cards

    def shuffle_desk(self):
        random.shuffle(self.cards)

    def get_card_by_index(self, index):
        if index < 0 or index >= len(self.cards):
            return None
        return self.cards.pop(index)


desk = CardDeck()
desk.shuffle_desk()

card_number = int(input('Choose card from 54 cards desk : '))
card = desk.get_card_by_index(card_number)
print(f'You card is: {card.return_cards()}')
print(len(desk.cards))

card_number = int(input('Choose card from 54 cards desk : '))
card = desk.get_card_by_index(card_number)
print(f'You card is: {card.return_cards()}')
print(len(desk.cards))
