import telebot
from extensions import API, APIException
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    instructions = """
    Привет! Я бот, который может вернуть цену на определенное количество валюты.
    Для получения цены отправьте мне сообщение в формате:
    <имя валюты цену которой вы хотите узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.
    Например: USD 10 RUB
    Для получения списка доступных валют используйте команду /values.
    """
    bot.reply_to(message, instructions)

@bot.message_handler(commands=['values'])
def handle_values(message):
    available_currencies = """
    Доступные валюты:
    - Евро (EUR)
    - Доллар (USD)
    - Рубль (RUB)
    """
    bot.reply_to(message, available_currencies)

@bot.message_handler(func=lambda message: True)
def handle_currency_conversion(message):
    # Получаем информацию из сообщения пользователя
    currency_input = message.text.split()
    if len(currency_input) == 3:
        base_currency = currency_input[0].upper()
        target_currency = currency_input[2].upper()
        amount = currency_input[1]

        try:
            converted_amount = API.get_price(base_currency, target_currency, amount)
            result = f"{amount} {base_currency} = {converted_amount} {target_currency}"
            bot.reply_to(message, result)
        except APIException as e:
            bot.reply_to(message, f"Ошибка: {e.message}")
    else:
        bot.reply_to(message, "Неверный формат команды. Проверьте инструкции команды /start.")

@bot.message_handler(func=lambda message: True)
def handle_error(message):
    try:
        raise APIException("Ошибка обработки команды.")
    except APIException as e:
        bot.reply_to(message, f"Ошибка: {e.message}")

bot.polling()
