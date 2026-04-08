"""
Task 2: Конвертер валют
Добавьте новый класс CurrencyConverter,
который умеет конвертировать различные валюты(USD, EUR, ...) в заданную валюту.
"""


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
