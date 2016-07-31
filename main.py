# -*- coding: utf-8 -*-
import telebot
from telebot import types

from .constants import USER_REGISTERED, USER_WELCOME
from .conf import TELEGRAM_TOKEN as TOKEN


bot = telebot.TeleBot(TOKEN)
rcadmin = '@rcotrina94'
dcadmin = '@dccm______'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, USER_WELCOME)
    bot.send_message(message.chat.id, USER_REGISTERED.format(message.chat.first_name))
    markup = types.ForceReply(selective=False)
    msg = bot.reply_to(message, u"¿Cuál es tu nombre completo?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        if chat_id not in user_dict:
            user_dict[chat_id] = user
            print "Usuario nuevo registrado"
        else:
            print "Usuario existente"
    except Exception:
        bot.reply_to(message, 'oooops')


@bot.message_handler(regexp='[Hh][Oo][Ll][Aa][!\?]*')
def say_hello(message):
    bot.send_message(message.chat.id, "Hola.")


@bot.message_handler(regexp='.*(tu(s)*(\s)+creador(es)*).*')
def send_creator_info(message):
    bot.send_message(message.chat.id, "Pues...")
    bot.send_message(message.chat.id, "Richard Cotrina ({}) y Carolina Morachimo ({})".format(rcadmin, dcadmin))


@bot.message_handler(commands=['help', 'ayuda'])
def help_message(message):
    bot.send_message(message.chat.id, u"Aquí debe mostrarse un mensaje de ayuda")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # bot.send_chat_action(message.chat.id, action='typing')
    # bot.reply_to(message, u"No te entiendo ¿Qué se supone que significa {}?".format(message.text))
    bot.send_message(message.chat.id, u"😆")


def handle_messages(messages):
    for message in messages:
        print u"{0}: {1}".format(message.chat.first_name, message.text)

bot.set_update_listener(handle_messages)

bot.polling()
