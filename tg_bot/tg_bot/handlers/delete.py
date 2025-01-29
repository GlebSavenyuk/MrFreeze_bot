from telebot import TeleBot
from storage import delete_product

def register_delete_handler(bot: TeleBot):
    @bot.message_handler(commands=['delete'])
    def handle_delete(message):
        bot.send_message(message.chat.id, "Введите название продукта, который хотите удалить:")
        bot.register_next_step_handler(message, process_delete)

    def process_delete(message):
        product_name = message.text
        delete_product(product_name)
        bot.send_message(message.chat.id, f"Продукт {product_name} удален (если он был в списке).")