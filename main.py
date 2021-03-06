import telebot
import buttons

bot = telebot.TeleBot('5039162809:AAHTB2UrrwjhK3-SQN2cbLs211UIS_OwUW4')

from telebot import types

global answer
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        keyboard = types.InlineKeyboardMarkup()
        key_start = types.InlineKeyboardButton(text='Узнать расписание', callback_data='key_start')
        keyboard.add(key_start)

        bot.send_message(message.from_user.id, 'Привет. Я Тайм-тян! Я помогу тебе узнать или вспомнить своё расписание, ~нян. \n \n Нажми на кнопку, чтобы узнать расписание, ~нян', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    elif message.text == "Привет":
        keyboard = types.InlineKeyboardMarkup()
        key_10 = types.InlineKeyboardButton(text='10', callback_data='key_10')
        keyboard.add(key_10)

        key_11 = types.InlineKeyboardButton(text='11', callback_data='key_11')
        keyboard.add(key_11)

        bot.send_message(message.from_user.id, "Привет! Выбери свой класс", reply_markup=keyboard)
    elif message.text == "Secret command":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Первый создатель любит "Евангелион"', callback_data='key_secr1')
        keyboard.add(key_1)
        key_2 = types.InlineKeyboardButton(text='Второй создатель любит kpop (Blink)', callback_data='key_secr2')
        keyboard.add(key_2)
        key_3 = types.InlineKeyboardButton(text='Третий создатель любит Java', callback_data='key_secr3')
        keyboard.add(key_3)

        bot.send_message(message.from_user.id, "Привет от разработчиков!", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, ~нян. Напиши /help, чтобы узнать мои возможности")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    buttons.buttons_call(call, bot)

bot.polling(none_stop=True, interval=0)

#lyc_sch_bot