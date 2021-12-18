import numpy as np
import tg_token
import telebot
import time
import random
from telebot import types
from male_rec import rec_nahui_list, rec_link_list
from male_models import maleGen, male_calls, male_angers


bot = telebot.TeleBot(tg_token.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    time.sleep(1)
    bot.send_message(message.chat.id, 'Ну здравствуй, ' + maleGen.maleRandList(male_calls) + ' ' + maleGen.maleRandList(male_angers))
    time.sleep(3)
    sent_len = len(maleGen.maleWordGen())
    if sent_len <= 50:

        time.sleep(4.9)
        bot.send_message(message.chat.id, maleGen.maleWordGen())
    if 50 < sent_len <= 70:
        time.sleep(5.8)
        bot.send_message(message.chat.id, maleGen.maleWordGen())
    if 70 < sent_len <=100:
        time.sleep(7)
        bot.send_message(message.chat.id, maleGen.maleWordGen())
    if sent_len > 100:
        time.sleep(9.1)
        bot.send_message(message.chat.id, maleGen.maleWordGen())

@bot.message_handler(content_types=['photo'])
def photo_sended(message):

    time.sleep(4)
    bot.send_message(message.chat.id, maleGen.maleOutsGen(2))
@bot.message_handler(content_types=['text'])
def outputs(message):
    if message.chat.type == 'private':



        for message_rec_link_list in rec_link_list:
            if message_rec_link_list in message.text:
                time.sleep(4)
                bot.send_message(message.chat.id, maleGen.maleOutsGen(0))

        for message_rec_nahui_list in rec_nahui_list:
            if message_rec_nahui_list in message.text:
                time.sleep(2.7)
                bot.send_message(message.chat.id, maleGen.maleOutsGen(3))

        if True:
            print(1)
            sent_len = len(maleGen.maleWordGen())
            if sent_len <= 50:
                time.sleep(4)
                bot.send_message(message.chat.id, maleGen.maleWordGen())
            if 50 < sent_len <= 70:
                time.sleep(5)
                bot.send_message(message.chat.id, maleGen.maleWordGen())
            if 70 < sent_len <= 100:
                time.sleep(6)
                bot.send_message(message.chat.id, maleGen.maleWordGen())
            if sent_len > 100:
                time.sleep(8)
                bot.send_message(message.chat.id, maleGen.maleWordGen())



bot.polling(none_stop = True)