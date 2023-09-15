import telebot
from telebot import types


bot = telebot.TeleBot('6666479317:AAEzbNZQhN3THMJd9ww2g7_1JqG9Q45CNPA')

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(" Доставка бухла")
    markup.add(btn1)
    bot.send_message(message.from_user.id, f"👋 Привет {message.from_user.first_name}", reply_markup=markup)
    bot.send_message(message.from_user.id, '👀 Выберите услугу')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #Русский язык
    if message.text == '🇷🇺 Доставка бухла':
        bot.send_message(message.from_user.id, f"{message.from_user.first_name}, cегодня доставка бухла не работает. Пиздуй в магазин!", parse_mode='html')
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
# echo-функция, которая отвечает на любое текстовое сообщение таким же текстом

bot.polling(non_stop=True, interval=0) #запуск бота