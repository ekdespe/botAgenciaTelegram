#!/usr/bin/python
#-*- coding: utf-8 -*- 
import telegram
#from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler
import os

myTocken ="354690332:AAFB8Dgjae9nLjbOlwbJHDSczCOXFKP-ybo"


def ajuda(bot, update):
    text = "/quemtaai - Lista todos os membros da agência presentes\n/ajuda - exibe este menu\n/info - exibe informações sobre o desenvolvedor"
    bot.sendMessage(update.message.chat_id, text)

def quemtaai(bot , update):
	os.system("./buscaNomes.sh")
   	
	arq = open("listaNomes.txt","r")
	texto = arq.read();
	arq.close()
    
	bot.sendMessage(update.message.chat_id, texto)


def info(bot , update):
    text = "Erik Ferreira - ekdespe@gmail.com \n @ekdespe \n 71 9.8277-6545 "
    bot.sendMessage(update.message.chat_id, text)

updater = Updater(myTocken)


updater.dispatcher.add_handler(CommandHandler('ajuda', ajuda))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('quemtaai', quemtaai))


updater.start_polling()
updater.idle()




