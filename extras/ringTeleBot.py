import telebot
from ringGUI import *

import sys

readyTeleMsg = """[telering v1] ready!"""

bot = telebot.TeleBot('2060666245:AAGxt0RTyFYRkCoyAUKGgS53gpHPe0iEyO8')
# -643011220
@bot.message_handler(commands=['ring'])
def all(message):
  ring_all()
  bot.send_message(message.chat.id, "🔔 Successfully Rung Braden's Doorbell.")

@bot.message_handler(commands=['choose', 'pick'])
def ringpick(message, arg1):
  choice = arg1

  if choice == 'chimes':
    playring('motion')
  if choice == 'ring' or 'ding':
    playring('ding')

@bot.message_handler(commands=['ringtest', 'test'])
def testring(message):
  ring_all_test()
  print(message.chat.id)
  bot.send_message(message.chat.id, "🔔 Successfully Rung Braden's Doorbell. (test)")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['stopbot'])
def stop():
  sys.exit()

bot.polling()