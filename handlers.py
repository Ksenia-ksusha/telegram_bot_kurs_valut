from config import bot, keyboard
from kursvalut import get_rates


@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = 'Привет, я бот, который показывает курс валют.' 
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
    
@bot.message_handler(regexp='Курс USD')
def send_kurs(message):
    text = get_rates()
    bot.send_message(message.chat.id, text, reply_markup=keyboard)    
    

@bot.message_handler(regexp='О проекте')
def send_about(message):
    text = 'Бот позволяет узнать курс валют на текущий день.\n' + \
           'Для получения курса валюты отправьте боту знак валюты.\n' + \
           'Бот использует сервис центробанка'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(regexp='Рекомендации')
def send_infa(message):
    text = 'Сейчас подберем информацию для Вас'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
