import telebot
import config
import random
import time

from telebot import types

bot = telebot.TeleBot(config.API_TOKEN)


@bot.message_handler(commands=['ya'])
def lol(message):
    bot.send_message(message.chat.id, "{0.first_name}!\n уехал.".format(
                message.from_user, bot.get_me()))





@bot.message_handler(commands=['start'])
def welcome(message):


    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/Я")
    item2 = types.KeyboardButton("/ПРИНЯЛ +")
    item3 = types.KeyboardButton("/БАРДЮР")
    item4 = types.KeyboardButton("/УЕХАЛ")
    item5 = types.KeyboardButton("/СВОБОДЕН ")
    item6 = types.KeyboardButton("/ПЕРСОНАЛЬНЫЙ ")
    item7 = types.KeyboardButton("/ИНФОРМАЦИЯ")

    markup.add(item1, item2,item3,item4,item5,item6, item7)





    bot.send_message(message.chat.id, text="taxi   ", reply_markup=markup)







            # RUN


bot.polling(none_stop=True)