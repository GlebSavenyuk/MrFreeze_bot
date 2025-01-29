from telebot import TeleBot
from storage import clear

def register_clear_handler(bot: TeleBot):
    @bot.message_handler(commands=['clear'])
    def hendler_clear(message):
        bot.send_message(message.chat.id, "Вы точно хотите очистить список: да/нет")
        bot.register_next_step_handler(message, process_clear_confirmation)

    def process_clear_confirmation(message):
        if message.text.lower() == 'да':
            clear()  
            bot.send_message(message.chat.id, "Список успешно очищен.")  
        elif message.text.lower() == 'нет':
            bot.send_message(message.chat.id, "Очистка списка отменена.")
        else:
            bot.send_message(message.chat.id, "Пожалуйста, ответьте 'да' или 'нет'.")
            bot.register_next_step_handler(message, process_clear_confirmation)
                