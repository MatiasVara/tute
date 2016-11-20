#!/usr/bin/python
# tute.py
#
import pprint
from telegram.ext import Updater
updater = Updater (token= 'YOURKEY')
dispatcher = updater.dispatcher
import logging
logging.basicConfig (format='%(asctime)s - %(message)s',
		     level=logging.INFO)

def hola(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.from_user.first_name+ " !!!" +" Como andas?")	
	logging.info("hola from: %s" % (update.message.from_user.first_name))

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Bienvenido!")
	logging.info("started with: %s" % (update.message.from_user.first_name))

from telegram.ext import CommandHandler


hi_handler = CommandHandler('hola', hola)
dispatcher.add_handler(hi_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler (start_handler)

updater.start_polling()
