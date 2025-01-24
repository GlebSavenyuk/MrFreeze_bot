import telebot
from handlers.add import register_add_handler
from handlers.list import register_list_handler
from handlers.delete import register_delete_handler
from handlers.edit import register_edit_handler

TOKEN = '7457578271:AAFFuSALbwo3Ieh1MJwSe1kMTXIl0MVyoHs'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        "Привет! Я MrFreeze_bot. Вот что я умею:\n"
        "/add - Добавить продукт\n"
        "/delete - Удалить продукт\n"
        "/edit - Редактировать продукт\n"
        "/list - Показать список продуктов\n"
        "/notify - Настроить напоминания\n"
        "/clear - Очистить весь список продуктов\n"
        "/help - Показать список команд"
)


register_edit_handler(bot)
register_delete_handler(bot)
register_add_handler(bot)
register_list_handler(bot)
bot.polling(non_stop=True)