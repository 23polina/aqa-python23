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


def cards_desk_creation():
    cards = []
    for mast in Card.mast_list:
        for number in Card.number_list:
            cards.append(Card(number, mast))
    cards.append(Card("Jocker1", None))
    cards.append(Card("Jocker2", None))
    return cards


cards_desk = cards_desk_creation()


def get_card(cards_desk):
    card_choose = random.choice(cards_desk)
    cards_desk.remove(card_choose)
    return card_choose


user_answer = input("Do you want to play? Choose Yes or No ")
while user_answer == 'Yes':
    selected_cards = get_card(cards_desk)
    print(f"Your card is {selected_cards.return_cards()}")
    user_answer = input("Do you want to play? Choose Yes or No ")
else:
    print("See you next time")


# Task 2:
class CurrencyConverter:
    def __init__(self, EURtoUSD, USDtoEUR, EURtoBYN, USDtoBYN):
        self.EURtoUSD = EURtoUSD
        self.USDtoEUR = USDtoEUR
        self.EURtoBYN = EURtoBYN
        self.USDtoBYN = USDtoBYN


today_currency = CurrencyConverter(EURtoUSD=1.16, USDtoEUR=0.8652, EURtoBYN=3.39, USDtoBYN=2.94)

amount_currency_to_exchange = input("Enter the amount and currency with space you would like to exchange ")
amount_str, currency = amount_currency_to_exchange.split()
amount = float(amount_str)
currency_to_which_exchange = input("Specify to which currency you would like to exchange: EUR, USD or BYN ")

exchanged_amount = 0

# It was the first version:
# def currency_exchange(amount, currency, currency_to_which_exchange):
#     if not currency_to_which_exchange:
#         currency_to_which_exchange = 'BYN'
#     if currency == 'USD' and currency_to_which_exchange == 'EUR':
#         exchanged_amount = amount * today_currency.USDtoEUR
#         return f"Your amount is {exchanged_amount} EUR"
#     elif currency == 'EUR' and currency_to_which_exchange == 'USD':
#         exchanged_amount = amount * today_currency.EURtoUSD
#         return f"Your amount is {exchanged_amount} USD"
#     elif currency == 'USD' and currency_to_which_exchange == 'BYN':
#         exchanged_amount = amount * today_currency.USDtoBYN
#         return f"Your amount is {exchanged_amount} BYN"
#     elif currency == 'EUR' and currency_to_which_exchange == 'BYN':
#         exchanged_amount = amount * today_currency.EURtoBYN
#         return f"Your amount is {exchanged_amount} BYN"
#     else:
#         return "Invalid currency selection"
#
#
# print(currency_exchange(amount, currency, currency_to_which_exchange))
#
def currency_exchange(amount, currency, currency_to_which_exchange):
    rates = {
        ('USD', 'EUR'): today_currency.USDtoEUR,
        ('EUR', 'USD'): today_currency.EURtoUSD,
        ('USD', 'BYN'): today_currency.USDtoBYN,
        ('EUR', 'BYN'): today_currency.EURtoBYN
    }
    if not currency_to_which_exchange:
        currency_to_which_exchange = 'BYN'
    key = (currency, currency_to_which_exchange)
    if key in rates:
        exchanged_amount = amount * rates[key]
        return f"Your exchanged_amount is {exchanged_amount} {currency_to_which_exchange}"
    else:
        return "Invalid currency selection"


print(currency_exchange(amount, currency, currency_to_which_exchange))
