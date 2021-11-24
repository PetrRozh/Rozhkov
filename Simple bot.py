import telebot
from telebot import types
from math import *

token = "2136431578:AAHe4rfISUvK_X5ix_6Lr6pwHiu8asPXd68"
bot = telebot.TeleBot(token)

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("хочу", "не интересно", "кто тебя создал такого..?", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать синус любого угла? Узнать про наш университет А мотивирующую песенку послушать?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n /univer - узнать про университет \n /cos - посчитать косинус за тебя \n /music - прислать мотивирующую песенку')


@bot.message_handler(commands=['univer'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')


@bot.message_handler(commands=['cos'])
def start_message(message):
    bot.send_message(message.chat.id,"Жду от тебя число!;)")


@bot.message_handler(commands=['music'])
def start_message(message):
    bot.send_message(message.chat.id, "Лови мотивирующую музычку!!!")
    audio = open('C:\\Users\\DELL\\Desktop\\music\\music.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда скорее пробуй бота!!!')
    if message.text.lower() == "не интересно":
        bot.send_message(message.chat.id, 'Ок, но я тебя запомнил!!!')
    if message.text.lower() == "кто тебя создал такого..?":
        bot.send_message(message.chat.id, 'Великий человек. Зовут - Рожков Пётр.')
    if is_number(message.text):
        bot.send_message(message.chat.id, cos(float(message.text)))

bot.polling()

