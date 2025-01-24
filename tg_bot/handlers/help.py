from telebot import TeleBot


def register_help_handler(bot: TeleBot):
    @bot.message_handler(commands=['help'])
    def help_command(message):
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

        