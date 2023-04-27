from dotenv import load_dotenv
import telebot
import telebot.types as types

load_dotenv()

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

bot = telebot.TeleBot(BOT_TOKEN)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton('Курс USD'))
keyboard.add(types.KeyboardButton('Курс EUR'))
keyboard.add(types.KeyboardButton('Рекомендации'))
keyboard.add(types.KeyboardButton('О проекте'))
