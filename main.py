
from telebot import *
from random import choice
import time

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

token = '7122140070:AAGggG8Vut5rY1W6xzZ7-FuWVd9xU63ReTw'
bot = TeleBot(token=token)

rems = []


@bot.message_handler(commands=['start'])
def set_reminder(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Приветствуем в игре здесь вы можете есть, спать, играть, тренироваться.Так же вы можете нажать /button чтобы увидеть все функции.Сразу после этого сообщения вы увидите информацию про своего питомца')
    info(message)
    global money, hp, energy, happiness, satiety, name
    money = 0
    hp = 5
    energy = 100
    happiness = 100
    satiety = 100
    name = 'Эрен Йегер'


money = 0
hp = 5
energy = 100
happiness = 100
satiety = 100
name = 'Эрен Йегер'


def feed():
    global satiety,energy
    satiety += 70
    energy -= 5

def play():
    global energy,satiety,happiness,money
    happiness += 40
    energy -= 25
    satiety -= 30
    money += 5

def sleep():
    global happiness, energy, satiety
    satiety -= 30
    energy = 100
    happiness += 20


def training():
    global hp,energy,satiety,happiness
    hp += 1
    energy -= 40
    satiety -= 50
    happiness -= 20


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = InlineKeyboardMarkup(row_width=1)
    item_1 = InlineKeyboardButton('Пойти поесть',callback_data='feed')
    item_2 = InlineKeyboardButton('Играть',callback_data='play')
    item_3 = InlineKeyboardButton('Спать', callback_data='sleep')
    item_4 = InlineKeyboardButton('Начать тренировку',callback_data='training')
    item_5 = InlineKeyboardButton('Информация персонажа',callback_data='info')
    markup.add(item_1, item_2, item_3, item_4, item_5,)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите действие!', reply_markup= markup)

@bot.callback_query_handler(func = lambda x: x.data in ['feed','play','sleep','training'])
def game_handler(call):
    chat_id = call.message.chat.id
    if call.data == 'feed':
        feed()
        bot.send_message(chat_id, 'Я поел')
        check(call.message)
    elif call.data == 'play':
        play()
        bot.send_message(chat_id, 'Было весело')
        check(call.message)
    elif call.data == 'sleep':
        sleep()
        bot.send_message(chat_id, 'Спать приятно, но пора вставать')
        check(call.message)
    elif call.data == 'training':
        training()
        bot.send_message(chat_id, 'Тренировка была достаточно трудной, надо бы отдохнуть')
        check(call.message)
    #elif message.text == 'Информация персонажа':

@bot.callback_query_handler(func = lambda x: x.data == 'info')
def info(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, f'''Меня зовут: {name}.
Уровень здоровья: {hp}.
Уровень энергии: {energy}.
Уровень счастья: {happiness}.
Уровень сытости: {satiety}.
Кол-во монет: {money}.
''')


def check(message):
    death = False
    global satiety, energy, happiness
    if satiety <= 0:
       death = True
       bot.send_message(message.chat.id, f'{name} умер от голода. Не забывайте кормить питомца!')
    elif satiety >= 10:
       bot.send_message(message.chat.id, f'{name} наелся и счастлив!')
    if happiness < 0:
       death = True
       bot.send_message(message.chat.id, f'{name} умер от тоски. С питомцем нужно чаще играть!')
    elif happiness > 100:
       bot.send_message(message.chat.id, f'{name} счастлив как никогда')
    if energy < 0:
       death = True
       bot.send_message(message.chat.id, f'{name} умер от истощения.’')
    elif energy > 70:
       bot.send_message(message.chat.id, f'{name} полон сил и энергии!!')
    if death:
      photo = open(r"Без имени.jpg", 'rb')
      bot.send_photo(message.chat.id, photo=photo)
      set_reminder(message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
   if call.message:
       if call.data=='':
           bot.send_message(call.message.chat.id, )
       elif call.data=='':
           bot.send_message(call.message.chat.id, )



bot.polling()
