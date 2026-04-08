"""
Task 1: Колода карт
Напишите программу которая содержит список карт,
умеет их перемешивать и позволяет пользователю достать карту из колоды по ее номеру.
Всего в колоде 54 карт. Класс Card содержит спискок номеров карт и список мастей.

Task 2: Конвертер валют
Добавьте новый класс CurrencyConverter,
который умеет конвертировать различные валюты(USD, EUR, ...) в заданную валюту.
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
        card_choose = self.cards[index]
        del self.cards[index]
        return card_choose


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


# Task 2:
class CurrencyConverter:
    def __init__(self, eur_to_usd, usd_to_eur, eur_to_byn, usd_to_byn):
        self.eur_to_usd = eur_to_usd
        self.usd_to_eur = usd_to_eur
        self.eur_to_byn = eur_to_byn
        self.usd_to_byn = usd_to_byn

    def currency_exchange(self, amt, cur, currency_exch):
        rates = {
            ('USD', 'EUR'): today_currency.usd_to_eur,
            ('EUR', 'USD'): today_currency.eur_to_usd,
            ('USD', 'BYN'): today_currency.usd_to_byn,
            ('EUR', 'BYN'): today_currency.eur_to_byn
        }
        if not currency_exch:
            currency_exch = 'BYN'
        key = (cur, currency_exch)
        if key in rates:
            exchanged_amount = amt * rates[key]
            return f"Your exchanged_amount is {exchanged_amount} {currency_exch}"
        else:
            return "Invalid currency selection"


today_currency = CurrencyConverter(
    eur_to_usd=1.16,
    usd_to_eur=0.8652,
    eur_to_byn=3.39,
    usd_to_byn=2.94)

amount_currency_to_exchange = input("Enter the amount and currency you would like to exchange ")
amount_str, currency = amount_currency_to_exchange.split()
amount = float(amount_str)
currency_to_which_exchange = input("Set currency you would like to exchange to: EUR, USD or BYN ")

print(today_currency.currency_exchange(amount, currency, currency_to_which_exchange))
