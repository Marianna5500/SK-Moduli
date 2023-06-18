import requests
import json

class APIException(Exception):
    def __init__(self, message):
        self.message = message

class API:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Неверно указано количество валюты. Пожалуйста, введите числовое значение.")

        # Отправляем запрос к API для получения курса валют
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
        data = json.loads(response.text)

        if quote in data['rates']:
            rate = data['rates'][quote]
            converted_amount = round(amount * rate, 2)
            return converted_amount
        else:
            raise APIException("Неверно указаны валюты. Проверьте команду /values для списка доступных валют.")
