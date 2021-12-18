from telebot import types
import json

def buttons_call(call, bot):
    if call.data == "key_10":
        keyboard10 = types.InlineKeyboardMarkup()
        key_MI = types.InlineKeyboardButton(text='МатИнфо', callback_data='key_10MI')
        keyboard10.add(key_MI)

        key_ME = types.InlineKeyboardButton(text='МатЭк', callback_data='key_10ME')
        keyboard10.add(key_ME)

        key_EN = types.InlineKeyboardButton(text='Естественные науки', callback_data='key_10EN')
        keyboard10.add(key_EN)

        bot.send_message(call.message.chat.id, "Выбери направление", reply_markup=keyboard10)
    elif call.data == "key_11":
        keyboard11 = types.InlineKeyboardMarkup()
        key_MI = types.InlineKeyboardButton(text='МатИнфо', callback_data='key_11MI')
        keyboard11.add(key_MI)

        key_ME = types.InlineKeyboardButton(text='МатЭк', callback_data='key_11ME')
        keyboard11.add(key_ME)

        key_EN = types.InlineKeyboardButton(text='Естественные науки', callback_data='key_11EN')
        keyboard11.add(key_EN)

        bot.send_message(call.message.chat.id, "Выбери направление", reply_markup=keyboard11)
    elif call.data == "key_10MI":
        keyboard11 = types.InlineKeyboardMarkup()
        key_10MI1gr = types.InlineKeyboardButton(text='1', callback_data='key_10MI1gr')
        keyboard11.add(key_10MI1gr)

        key_10MI2gr = types.InlineKeyboardButton(text='2', callback_data='key_10MI2gr')
        keyboard11.add(key_10MI2gr)

        key_10MI3gr = types.InlineKeyboardButton(text='3', callback_data='key_10MI3gr')
        keyboard11.add(key_10MI3gr)

        key_10MI4gr = types.InlineKeyboardButton(text='4', callback_data='key_10MI4gr')
        keyboard11.add(key_10MI4gr)

        bot.send_message(call.message.chat.id, "Выбери группу", reply_markup=keyboard11)
    elif call.data == "key_10ME":
        keyboard11 = types.InlineKeyboardMarkup()
        key_10ME1gr = types.InlineKeyboardButton(text='1', callback_data='key_10ME1gr')
        keyboard11.add(key_10ME1gr)

        key_10ME2gr = types.InlineKeyboardButton(text='2', callback_data='key_10ME2gr')
        keyboard11.add(key_10ME2gr)

        key_10ME3gr = types.InlineKeyboardButton(text='3', callback_data='key_10ME3gr')
        keyboard11.add(key_10ME3gr)

        key_10ME4gr = types.InlineKeyboardButton(text='4', callback_data='key_10ME4gr')
        keyboard11.add(key_10ME4gr)

        key_10ME5gr = types.InlineKeyboardButton(text='5', callback_data='key_10ME5gr')
        keyboard11.add(key_10ME5gr)

        bot.send_message(call.message.chat.id, "Выбери группу", reply_markup=keyboard11)
    elif call.data == "key_10EN":
        keyboard11 = types.InlineKeyboardMarkup()
        key_10EN1gr = types.InlineKeyboardButton(text='1', callback_data='key_10EN1gr')
        keyboard11.add(key_10EN1gr)

        key_10EN2gr = types.InlineKeyboardButton(text='2', callback_data='key_10EN2gr')
        keyboard11.add(key_10EN2gr)

        bot.send_message(call.message.chat.id, "Выбери группу", reply_markup=keyboard11)
    elif call.data == "key_11MI":
        keyboard11 = types.InlineKeyboardMarkup()
        key_11MI1gr = types.InlineKeyboardButton(text='1', callback_data='key_11MI1gr')
        keyboard11.add(key_11MI1gr)

        key_11MI2gr = types.InlineKeyboardButton(text='2', callback_data='key_11MI2gr')
        keyboard11.add(key_11MI2gr)

        key_11MI3gr = types.InlineKeyboardButton(text='3', callback_data='key_11MI3gr')
        keyboard11.add(key_11MI3gr)

        key_11MI4gr = types.InlineKeyboardButton(text='4', callback_data='key_11MI4gr')
        keyboard11.add(key_11MI4gr)

        bot.send_message(call.message.chat.id, "Выбери группу", reply_markup=keyboard11)
    elif call.data == "key_11ME":
        keyboard11 = types.InlineKeyboardMarkup()
        key_11ME1gr = types.InlineKeyboardButton(text='1', callback_data='key_11ME1gr')
        keyboard11.add(key_11ME1gr)

        key_11ME2gr = types.InlineKeyboardButton(text='2', callback_data='key_11ME2gr')
        keyboard11.add(key_11ME2gr)

        key_11ME3gr = types.InlineKeyboardButton(text='3', callback_data='key_11ME3gr')
        keyboard11.add(key_11ME3gr)

        key_11ME4gr = types.InlineKeyboardButton(text='4', callback_data='key_11ME4gr')
        keyboard11.add(key_11ME4gr)

        key_11ME5gr = types.InlineKeyboardButton(text='5', callback_data='key_11ME5gr')
        keyboard11.add(key_11ME5gr)

        bot.send_message(call.message.chat.id, "Выбери направление", reply_markup=keyboard11)
    elif call.data == "key_11EN":
        keyboard11 = types.InlineKeyboardMarkup()
        key_11EN1gr = types.InlineKeyboardButton(text='1', callback_data='key_11EN1gr')
        keyboard11.add(key_11EN1gr)

        key_11EN2gr = types.InlineKeyboardButton(text='2', callback_data='key_11EN2gr')
        keyboard11.add(key_11EN2gr)

        bot.send_message(call.message.chat.id, "Выбери группу", reply_markup=keyboard11)

    # TODO кнопки выбора дня недели
    elif call.data == "key_10MI1gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10MI1grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10MI1grMon')
        keyboard10d.add(key_10MI1grMon)

        key_10MI1grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10MI1grTue')
        keyboard10d.add(key_10MI1grTue)

        key_10MI1grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10MI1grWed')
        keyboard10d.add(key_10MI1grWed)

        key_10MI1grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10MI1grThu')
        keyboard10d.add(key_10MI1grThu)

        key_10MI1grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10MI1grFri')
        keyboard10d.add(key_10MI1grFri)

        key_10MI1grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10MI1grSat')
        keyboard10d.add(key_10MI1grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10MI2gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10MI2grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10MI2grMon')
        keyboard10d.add(key_10MI2grMon)

        key_10MI2grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10MI2grTue')
        keyboard10d.add(key_10MI2grTue)

        key_10MI2grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10MI2grWed')
        keyboard10d.add(key_10MI2grWed)

        key_10MI2grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10MI2grThu')
        keyboard10d.add(key_10MI2grThu)

        key_10MI2grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10MI2grFri')
        keyboard10d.add(key_10MI2grFri)

        key_10MI2grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10MI2grSat')
        keyboard10d.add(key_10MI2grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10MI3gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10MI3grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10MI3grMon')
        keyboard10d.add(key_10MI3grMon)

        key_10MI3grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10MI3grTue')
        keyboard10d.add(key_10MI3grTue)

        key_10MI3grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10MI3grWed')
        keyboard10d.add(key_10MI3grWed)

        key_10MI3grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10MI3grThu')
        keyboard10d.add(key_10MI3grThu)

        key_10MI3grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10MI3grFri')
        keyboard10d.add(key_10MI3grFri)

        key_10MI3grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10MI3grSat')
        keyboard10d.add(key_10MI3grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10MI4gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10MI4grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10MI4grMon')
        keyboard10d.add(key_10MI4grMon)

        key_10MI4grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10MI4grTue')
        keyboard10d.add(key_10MI4grTue)

        key_10MI4grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10MI4grWed')
        keyboard10d.add(key_10MI4grWed)

        key_10MI4grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10MI4grThu')
        keyboard10d.add(key_10MI4grThu)

        key_10MI4grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10MI4grFri')
        keyboard10d.add(key_10MI4grFri)

        key_10MI4grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10MI4grSat')
        keyboard10d.add(key_10MI4grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10ME1gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10ME1grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10ME1grMon')
        keyboard10d.add(key_10ME1grMon)

        key_10ME1grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10ME1grTue')
        keyboard10d.add(key_10ME1grTue)

        key_10ME1grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10ME1grWed')
        keyboard10d.add(key_10ME1grWed)

        key_10ME1grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10ME1grThu')
        keyboard10d.add(key_10ME1grThu)

        key_10ME1grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10ME1grFri')
        keyboard10d.add(key_10ME1grFri)

        key_10ME1grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10ME1grSat')
        keyboard10d.add(key_10ME1grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10ME2gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10ME2grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10ME2grMon')
        keyboard10d.add(key_10ME2grMon)

        key_10ME2grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10ME2grTue')
        keyboard10d.add(key_10ME2grTue)

        key_10ME2grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10ME2grWed')
        keyboard10d.add(key_10ME2grWed)

        key_10ME2grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10ME2grThu')
        keyboard10d.add(key_10ME2grThu)

        key_10ME2grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10ME2grFri')
        keyboard10d.add(key_10ME2grFri)

        key_10ME2grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10ME2grSat')
        keyboard10d.add(key_10ME2grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10ME3gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10ME3grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10ME3grMon')
        keyboard10d.add(key_10ME3grMon)

        key_10ME3grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10ME3grTue')
        keyboard10d.add(key_10ME3grTue)

        key_10ME3grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10ME3grWed')
        keyboard10d.add(key_10ME3grWed)

        key_10ME3grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10ME3grThu')
        keyboard10d.add(key_10ME3grThu)

        key_10ME3grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10ME3grFri')
        keyboard10d.add(key_10ME3grFri)

        key_10ME3grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10ME3grSat')
        keyboard10d.add(key_10ME3grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10ME4gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10ME4grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10ME4grMon')
        keyboard10d.add(key_10ME4grMon)

        key_10ME4grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10ME4grTue')
        keyboard10d.add(key_10ME4grTue)

        key_10ME4grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10ME4grWed')
        keyboard10d.add(key_10ME4grWed)

        key_10ME4grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10ME4grThu')
        keyboard10d.add(key_10ME4grThu)

        key_10ME4grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10ME4grFri')
        keyboard10d.add(key_10ME4grFri)

        key_10ME4grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10ME4grSat')
        keyboard10d.add(key_10ME4grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10ME5gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10ME5grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10ME5grMon')
        keyboard10d.add(key_10ME5grMon)

        key_10ME5grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10ME5grTue')
        keyboard10d.add(key_10ME5grTue)

        key_10ME5grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10ME5grWed')
        keyboard10d.add(key_10ME5grWed)

        key_10ME5grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10ME5grThu')
        keyboard10d.add(key_10ME5grThu)

        key_10ME5grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10ME5grFri')
        keyboard10d.add(key_10ME5grFri)

        key_10ME5grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10ME5grSat')
        keyboard10d.add(key_10ME5grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10EN1gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10EN1grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10EN1grMon')
        keyboard10d.add(key_10EN1grMon)

        key_10EN1grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10EN1grTue')
        keyboard10d.add(key_10EN1grTue)

        key_10EN1grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10EN1grWed')
        keyboard10d.add(key_10EN1grWed)

        key_10EN1grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10EN1grThu')
        keyboard10d.add(key_10EN1grThu)

        key_10EN1grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10EN1grFri')
        keyboard10d.add(key_10EN1grFri)

        key_10EN1grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10EN1grSat')
        keyboard10d.add(key_10EN1grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_10EN2gr":
        keyboard10d = types.InlineKeyboardMarkup()
        key_10EN2grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10EN2grMon')
        keyboard10d.add(key_10EN2grMon)

        key_10EN2grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10EN2grTue')
        keyboard10d.add(key_10EN2grTue)

        key_10EN2grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10EN2grWed')
        keyboard10d.add(key_10EN2grWed)

        key_10EN2grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10EN2grThu')
        keyboard10d.add(key_10EN2grThu)

        key_10EN2grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10EN2grFri')
        keyboard10d.add(key_10EN2grFri)

        key_10EN2grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10EN2grSat')
        keyboard10d.add(key_10EN2grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard10d)
    elif call.data == "key_11MI1gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11MI1grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11MI1grMon')
        keyboard11d.add(key_11MI1grMon)

        key_11MI1grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11MI1grTue')
        keyboard11d.add(key_11MI1grTue)

        key_11MI1grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11MI1grWed')
        keyboard11d.add(key_11MI1grWed)

        key_11MI1grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11MI1grThu')
        keyboard11d.add(key_11MI1grThu)

        key_11MI1grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11MI1grFri')
        keyboard11d.add(key_11MI1grFri)

        key_11MI1grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11MI1grSat')
        keyboard11d.add(key_11MI1grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11MI2gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11MI2grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11MI2grMon')
        keyboard11d.add(key_11MI2grMon)

        key_11MI2grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11MI2grTue')
        keyboard11d.add(key_11MI2grTue)

        key_11MI2grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11MI2grWed')
        keyboard11d.add(key_11MI2grWed)

        key_11MI2grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11MI2grThu')
        keyboard11d.add(key_11MI2grThu)

        key_11MI2grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11MI2grFri')
        keyboard11d.add(key_11MI2grFri)

        key_11MI2grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11MI2grSat')
        keyboard11d.add(key_11MI2grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11MI3gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_10MI3grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_10MI3grMon')
        keyboard11d.add(key_10MI3grMon)

        key_10MI3grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_10MI3grTue')
        keyboard11d.add(key_10MI3grTue)

        key_10MI3grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_10MI3grWed')
        keyboard11d.add(key_10MI3grWed)

        key_10MI3grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_10MI3grThu')
        keyboard11d.add(key_10MI3grThu)

        key_10MI3grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_10MI3grFri')
        keyboard11d.add(key_10MI3grFri)

        key_10MI3grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_10MI3grSat')
        keyboard11d.add(key_10MI3grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11MI4gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11MI4grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11MI4grMon')
        keyboard11d.add(key_11MI4grMon)

        key_11MI4grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11MI4grTue')
        keyboard11d.add(key_11MI4grTue)

        key_11MI4grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11MI4grWed')
        keyboard11d.add(key_11MI4grWed)

        key_11MI4grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11MI4grThu')
        keyboard11d.add(key_11MI4grThu)

        key_11MI4grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11MI4grFri')
        keyboard11d.add(key_11MI4grFri)

        key_11MI4grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11MI4grSat')
        keyboard11d.add(key_11MI4grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11ME1gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11ME1grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11ME1grMon')
        keyboard11d.add(key_11ME1grMon)

        key_11ME1grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11ME1grTue')
        keyboard11d.add(key_11ME1grTue)

        key_11ME1grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11ME1grWed')
        keyboard11d.add(key_11ME1grWed)

        key_11ME1grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11ME1grThu')
        keyboard11d.add(key_11ME1grThu)

        key_11ME1grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11ME1grFri')
        keyboard11d.add(key_11ME1grFri)

        key_11ME1grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11ME1grSat')
        keyboard11d.add(key_11ME1grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11ME2gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11ME2grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11ME2grMon')
        keyboard11d.add(key_11ME2grMon)

        key_11ME2grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11ME2grTue')
        keyboard11d.add(key_11ME2grTue)

        key_11ME2grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11ME2grWed')
        keyboard11d.add(key_11ME2grWed)

        key_11ME2grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11ME2grThu')
        keyboard11d.add(key_11ME2grThu)

        key_11ME2grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11ME2grFri')
        keyboard11d.add(key_11ME2grFri)

        key_11ME2grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11ME2grSat')
        keyboard11d.add(key_11ME2grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11ME3gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11ME3grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11ME3grMon')
        keyboard11d.add(key_11ME3grMon)

        key_11ME3grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11ME3grTue')
        keyboard11d.add(key_11ME3grTue)

        key_11ME3grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11ME3grWed')
        keyboard11d.add(key_11ME3grWed)

        key_11ME3grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11ME3grThu')
        keyboard11d.add(key_11ME3grThu)

        key_11ME3grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11ME3grFri')
        keyboard11d.add(key_11ME3grFri)

        key_11ME3grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11ME3grSat')
        keyboard11d.add(key_11ME3grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11ME4gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11ME4grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11ME4grMon')
        keyboard11d.add(key_11ME4grMon)

        key_11ME4grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11ME4grTue')
        keyboard11d.add(key_11ME4grTue)

        key_11ME4grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11ME4grWed')
        keyboard11d.add(key_11ME4grWed)

        key_11ME4grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11ME4grThu')
        keyboard11d.add(key_11ME4grThu)

        key_11ME4grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11ME4grFri')
        keyboard11d.add(key_11ME4grFri)

        key_11ME4grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11ME4grSat')
        keyboard11d.add(key_11ME4grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11ME5gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11ME5grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11ME5grMon')
        keyboard11d.add(key_11ME5grMon)

        key_11ME5grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11ME5grTue')
        keyboard11d.add(key_11ME5grTue)

        key_11ME5grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11ME5grWed')
        keyboard11d.add(key_11ME5grWed)

        key_11ME5grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11ME5grThu')
        keyboard11d.add(key_11ME5grThu)

        key_11ME5grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11ME5grFri')
        keyboard11d.add(key_11ME5grFri)

        key_11ME5grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11ME5grSat')
        keyboard11d.add(key_11ME5grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11EN1gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11EN1grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11EN1grMon')
        keyboard11d.add(key_11EN1grMon)

        key_11EN1grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11EN1grTue')
        keyboard11d.add(key_11EN1grTue)

        key_11EN1grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11EN1grWed')
        keyboard11d.add(key_11EN1grWed)

        key_11EN1grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11EN1grThu')
        keyboard11d.add(key_11EN1grThu)

        key_11EN1grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11EN1grFri')
        keyboard11d.add(key_11EN1grFri)

        key_11EN1grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11EN1grSat')
        keyboard11d.add(key_11EN1grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)
    elif call.data == "key_11EN2gr":
        keyboard11d = types.InlineKeyboardMarkup()
        key_11EN2grMon = types.InlineKeyboardButton(text='Понедельник', callback_data='key_11EN2grMon')
        keyboard11d.add(key_11EN2grMon)

        key_11EN2grTue = types.InlineKeyboardButton(text='Вторник', callback_data='key_11EN2grTue')
        keyboard11d.add(key_11EN2grTue)

        key_11EN2grWed = types.InlineKeyboardButton(text='Среда', callback_data='key_11EN2grWed')
        keyboard11d.add(key_11EN2grWed)

        key_11EN2grThu = types.InlineKeyboardButton(text='Четверг', callback_data='key_11EN2grThu')
        keyboard11d.add(key_11EN2grThu)

        key_11EN2grFri = types.InlineKeyboardButton(text='Пятница', callback_data='key_11EN2grFri')
        keyboard11d.add(key_11EN2grFri)

        key_11EN2grSat = types.InlineKeyboardButton(text='Суббота', callback_data='key_11EN2grSat')
        keyboard11d.add(key_11EN2grSat)

        bot.send_message(call.message.chat.id, "Выбери день недели", reply_markup=keyboard11d)

    # TODO расписание


    elif call.data == "key_1":
        bot.send_message(call.message.chat.id, "Молодец! Туда и иди, и не смей возвращаться, блядина")
        bot.send_photo()
        bot.send_audio()
    elif call.data == "key_secr1":
        photo = open(r'evangelion.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        photo.close()
    elif call.data == "key_secr2":
        photo = open(r'blackpink.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        photo.close()
        audio = open(r'blackpink.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
        audio.close()
    elif call.data == "key_secr3":
        audio = open(r'Java Is What Java Does.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
        audio.close()

with open("database.json") as database_file:
    data = database_file.read()