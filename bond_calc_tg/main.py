import random

import telebot
from telebot import types

import logging

#Токен бота
bot = telebot.TeleBot('6426652110:AAEhnkXDCFDmcj905H0L8oUqcSdjWvXW4yk')
#Для проверки бота когда ставишь на хост
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logging.info("Starting bot")
#Для работы команд start и help
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Wassup Dude \nНапиши /help, чтобы узнать возможности бота")
    sticker_list = ['CAACAgQAAxkBAAIPMmE7qLcdcV9Hppmu2tkqP9AX_BfWAALdFAACOYBWBoQhW4WPbkZEIAQ',
                    'CAACAgQAAxkBAAIPPmE7qmrY9NMaij3_NYJ82-kk60Y2AAJ4CQAC3kD4B58Jvr39YNpvIAQ']
    sticker = random.choice(sticker_list)



    bot.send_sticker(message.chat.id, sticker)
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,"Данный бот может считать облигации")
@bot.message_handler(commands=['work'])
def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def call(call):
    if call=='':
        bot.send_message('Начало положено')
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Кнопка":
        bot.send_message(message.chat.id, 'Е бади')

bot.polling(none_stop=True, interval=0)

