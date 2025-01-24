from telebot import TeleBot
from storage import add_product


def register_add_handler(bot: TeleBot):
    @bot.message_handler(commands=['add'])
    def handle_add(message):
        bot.send_message(message.chat.id,
            "Введите данные продукта в формате: название, срок годности Д-М-Г, количество.\n"
            "Пример: молоко, 15-01-2025, 2\n"
            "Или просто: хлеб"
        )
        bot.register_next_step_handler(message, process_add)

    def process_add(message):
        try:
            data = message.text.split(', ')
            name = data[0]
            if name.startswith('/'):
                raise ValueError()
            expiration_date = None
            quantity = 1
            n = len(data)

            if n > 1:
                expiration_date = data[1]
            if n > 2:
                quantity = int(data[2])

            add_product(name, expiration_date, quantity)

            response = f'Продукт {name} добавлен!'
            if expiration_date:
                response += f" Срок годности: {expiration_date}."
            response += f" Количество: {quantity}."
            bot.send_message(message.chat.id, response)

        except Exception as e:
            bot.send_message(message.chat.id, "Неверный формат. Попробуйте снова.")
            handle_add(message)  
