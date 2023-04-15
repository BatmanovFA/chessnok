# Подключение библиотек стандартных
import telebot
# from telebot import types

# Подключение собственно созданных библиотек
# import chessnok_alpha

# Подключение к ботам
Telegram_bot = telebot.TeleBot('6135051270:AAFM3_Fx-PrQBGIXxVrJS6Fkq4Kd-phCiAE')


# Получение и обработка текствоых сообщений
@Telegram_bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hi":
        Telegram_bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else:
        Telegram_bot.send_message(message.from_user.id, "G")


# Работа бота
def main():
    Telegram_bot.infinity_polling()


if __name__ == "__main__":
    main()
