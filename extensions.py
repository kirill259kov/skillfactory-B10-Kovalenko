import requests
import json
from config import exchanges

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")
        try:
            quote_key = exchanges[quote.lower()]
        except KeyError:
            raise APIException(f'Валюта {quote} не найдена!')
        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={quote_key}&from={base_key}&amount={amount}'
        payload = {}
        headers = {
            "apikey": "4CoexUy7LUNXa7xtLbICN1sAi3UoLQYP"
        }
        response = requests.request("GET", url, headers=headers)
        result = json.loads(response.content)['result']
        result = round(result, 1)
        mess = f"Цена {amount} {base} в {quote} : {result}"
        return mess


