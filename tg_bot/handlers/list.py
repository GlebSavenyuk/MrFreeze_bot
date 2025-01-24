from telebot import TeleBot
from storage import get_products

def register_list_handler(bot: TeleBot):
    @bot.message_handler(commands=['list'])
    def handle_list(message):
        products = get_products()
        if not products:
            bot.send_message(message.chat.id, "Список продуктов пуст.")
        else:
            response = "Ваши продукты:\n"
            for product in products:
                response += f"- {product['name']}"
                if product["expiration_date"]:
                    response += f", срок годности: {product['expiration_date']}"
                response += f", количество: {product['quantity']}\n"
            bot.send_message(message.chat.id, response)