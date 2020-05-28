import telebot
from telebot import types
import selecting
bot = telebot.TeleBot('token')
@bot.message_handler(commands=['start', 'menu'])
def welcome(message):
    # print(message)
    # bot.send_message(message.chat.id, "text")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but1 = types.KeyboardButton("9 класс")
    but2 = types.KeyboardButton("10 класс")
    but3 = types.KeyboardButton("11 класс")
    menu.add(but1, but2, but3)
    bot.send_message(message.chat.id, "Выбери класс:", reply_markup=menu)
classes = ['9 класс', '10 класс', '11 класс']
days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ']
cls = 0
@bot.message_handler(content_types=['text'])
def get_messages(message):
    if message.text in classes:
        global cls
        cls = message.text.split(' ')[0]
        # print(cls)
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("ПН")
        but2 = types.KeyboardButton("ВТ")
        but3 = types.KeyboardButton("СР")
        but4 = types.KeyboardButton("ЧТ")
        but5 = types.KeyboardButton("ПТ")
        menu.add(but1, but2, but3, but4, but5)
        bot.send_message(message.chat.id, "Выбери день недели:", reply_markup=menu)
    elif message.text in days:
        # pass
        day = message.text
        selecting.get_lessons(bot, message, cls, day)

bot.polling()
