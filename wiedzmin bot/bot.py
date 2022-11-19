import config
import logging
import random
from aiogram import Bot, Dispatcher, executor, types
import os, json, string
from db import Database
import asyncio
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
import sqlite3
import markups as nav

import time
import datetime

#log level
logging.basicConfig(level=logging.INFO)

#Инициализация бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')

#async def on_startup(_):
	#await bot.send_message(-1001373568416, "Я вернулся <b>(бот онлайн ✅)</b>", parse_mode="html")

#преобразователь минут в секунды
def minutes_to_seconds(minutes):
	return minutes * 60

#проверка оставшегося времени до следующей фермы
def time_ost(get_time):
	time_now = int(time.time())
	middle_time = int(get_time) - time_now

	if middle_time <= 0:
		return False
	else:
		dt = str(datetime.timedelta(seconds=middle_time))
		return dt



@dp.message_handler(commands=["mute"], commands_prefix="+")
async def mute(message: types.Message):
    if str(message.from_user.id) == config.ADMIN_ID or config.ADMIN_ID2 or config.ADMIN_ID3:
    	if not message.reply_to_message:
    	    await message.reply("Команда должна быть ответом на сообщение!")
    	    return
    	mute_sec = int(message.text[6:])
    	db.add_mute(message.reply_to_message.from_user.id, mute_sec)
    	await message.answer(f"Тестовый мут на {mute_sec} секунд")


    #основные функции фермы
@dp.message_handler()
async def filter_messages(message: types.Message):

    if message.text.lower() =="фарм":
        florens = random.randint(4, 50)
        bonus = random.randint(4, 50)
        if (not db.user_ex(message.from_user.id)): #проверка на присутствие пользователя в бд ferma
            current_datetime = int(time.time()) + minutes_to_seconds(180) #получение текущего времени в секундах + 3 часа до следующей фермы
            db.add_user(message.from_user.id, message.from_user.first_name, florens, current_datetime) #добавление пользователя в бд
            await message.answer("<b>🌞 | Вы заработали <u>" + str(florens) + "</u> флоренов!</b>", parse_mode='html', reply_markup=nav.Bonuses)
        else:
            user_time_ost = time_ost(db.get_time(message.from_user.id))
            if user_time_ost == False:
                if (not(db.bonus_ex(message.from_user.id))):
                    await message.answer("<b>🌞 | Вы заработали <u>" + str(florens) + "</u> флоренов!</b>", parse_mode='html', reply_markup=nav.Bonuses)
                    if (not(db.bonus2_ex(message.from_user.id))):
                        current_datetime = int(time.time()) + minutes_to_seconds(180)
                        db.set_time(current_datetime, message.from_user.id)
                        db.balance_update(int(db.get_balance(message.from_user.id)) + florens, message.from_user.first_name,message.from_user.id)
                    else:
                        current_datetime = int(time.time()) + minutes_to_seconds(120)
                        db.set_time(current_datetime, message.from_user.id)
                        db.balance_update(int(db.get_balance(message.from_user.id)) + florens, message.from_user.first_name, message.from_user.id)
                else:
                    await message.answer("<b>🌞 | Вы заработали <u>" + str(int(florens + bonus)) + "</u> флоренов!</b>\n" 
                    "<b>💎 | Бонусные " + str(bonus) + "</b>", parse_mode='html', reply_markup=nav.Bonuses)
                    if (not (db.bonus2_ex(message.from_user.id))):
                        current_datetime = int(time.time()) + minutes_to_seconds(180)
                        db.set_time(current_datetime, message.from_user.id)
                        db.balance_update(int(db.get_balance(message.from_user.id)) + florens, message.from_user.first_name, message.from_user.id)
                    else:
                        current_datetime = int(time.time()) + minutes_to_seconds(120)
                        db.set_time(current_datetime, message.from_user.id)
                        db.balance_update(int(db.get_balance(message.from_user.id)) + florens, message.from_user.first_name, message.from_user.id)
            else:
                if (not (db.bonus2_ex(message.from_user.id))):
                    await message.answer("<b>⛔️ | Время - деньги.\nДо следующего фарма: " + str(user_time_ost) + "</b>", parse_mode='html', reply_markup=nav.Bonuses)
                else:
                    await message.answer("<b>⛔🕊️ | Время - деньги.\nДо следующего фарма: " + str(user_time_ost) + "</b>", parse_mode='html', reply_markup=nav.Bonuses)

    if message.text.lower() == "мой баланс":
    	if (not db.user_ex(message.from_user.id)):
    		await message.answer("<b>Ваши кармашки пусты!</b>", parse_mode='html')
    	else:
            if db.bonus_ex(message.from_user.id) & db.bonus2_ex(message.from_user.id):
                user_balance = db.get_balance(message.from_user.id)
                await message.answer("<b>🪙 | Всего в кармане: <u>" + user_balance + "</u> флоренов</b>"
                '\n<b>⭐ | Бонусы:</b> Ласточка🕊, Вторая жизнь💎 ', parse_mode='html')

            elif db.bonus2_ex(message.from_user.id):
                user_balance = db.get_balance(message.from_user.id)
                await message.answer("<b>🪙 | Всего в кармане: <u>" + user_balance + "</u> флоренов</b>"
                '\n<b>⭐ | Бонусы:</b> Ласточка🕊', parse_mode='html')

            elif db.bonus_ex(message.from_user.id):
                user_balance = db.get_balance(message.from_user.id)
                await message.answer("<b>🪙 | Всего в кармане: <u>" + user_balance + "</u> флоренов</b>"
                '\n<b>⭐ | Бонусы:</b> Вторая жизнь💎', parse_mode='html')

            else:
                user_balance = db.get_balance(message.from_user.id)
                await message.answer("<b>🪙 | Всего в кармане: <u>" + user_balance + "</u> флоренов</b>", parse_mode='html')









    #реакция на слова
    if message.text.lower() == "я вернулся":
    	await message.reply('Откуда?')

    if message.text.lower() == "я вернулась":
        await message.reply('Откуда?')


    #рекация на слово рыжий
    text = message.text.lower()
    for word in config.WORDS_RIJIY:
        if word in text:
    	    await message.reply('Веди себя прилично, приблуда!')
    	    await message.delete()

    #рекация на слово ведьмак
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('who.json')))) != set():
        await message.reply('А кто это??')

    # топ флоренов чата
    if message.text.lower() == "топф":
	    await message.reply("📈<b> 15 БОГАТЕЙШИХ ЛЮДЕЙ:</b>" +'\n'+'\n'
        '1. 🥇 ' + (db.get_kollNAME())  + ' — ' + (str(db.get_koll())) +'\n'
        '2. 🥈 ' + (db.get_kollNAME2()) + ' — ' + (str(db.get_koll2()))+'\n'
        '3. 🥉 ' + (db.get_kollNAME3()) + ' — ' + (str(db.get_koll3()))+'\n'
        '4.  ' + (db.get_kollNAME4()) + ' — ' + (str(db.get_koll4()))+'\n'
        '5.  ' + (db.get_kollNAME5()) + ' — ' + (str(db.get_koll5()))+'\n'
        '6.  ' + (db.get_kollNAME6()) + ' — ' + (str(db.get_koll6()))+'\n'
        '7.  ' + (db.get_kollNAME7()) + ' — ' + (str(db.get_koll7()))+'\n'
        '8.  ' + (db.get_kollNAME8()) + ' — ' + (str(db.get_koll8()))+'\n'
        '9.  ' + (db.get_kollNAME9()) + ' — ' + (str(db.get_koll9()))+'\n'
        '10.  ' + (db.get_kollNAME10()) + ' — ' + (str(db.get_koll10()))+'\n'
        '11.  ' + (db.get_kollNAME11()) + ' — ' + (str(db.get_koll11()))+'\n'
        '12.  ' + (db.get_kollNAME12()) + ' — ' + (str(db.get_koll12()))+'\n'
        '13.  ' + (db.get_kollNAME13()) + ' — ' + (str(db.get_koll13()))+'\n'     
        '14.  ' + (db.get_kollNAME14()) + ' — ' + (str(db.get_koll14()))+'\n'                                                              
        '15.  ' + (db.get_kollNAME15()) + ' — ' + (str(db.get_koll15())), parse_mode='html')

    #вызов бонусов

    if message.text.lower() == "бонусы":
	    await message.answer('<b>⭐ СПИСОК ВСЕХ ДОСТУПНЫХ БОНУСОВ: </b>\n \n'
        '💎 №1 <b>Вторая жизнь</b> '
        '\nДает возможность получать флорены, как за два фарма.\n'
        '<i>Стоимость: 1500 флоренов</i>'
        '\n\n🕊 №2 <b>Ласточка</b>'
        '\nСнижает время до следующего фарма на один час.\n'
        '<i>Стоимость: 950 флоренов</i>'
        '\n\n💮 №3 <b>Лакомка</b> '
         '\nКаждые 4 часа начисляет флорены на ваш баланс. (не влияет '
         'на основное время и равноценно обычному фарму)\n'
         '<i>Стоимость: 10000 флоренов</i>'
         '\n\n<i>‼ бонусы выдаются навсегда</i>', parse_mode='html', reply_markup=nav.mainMenu)

    @dp.callback_query_handler(text_contains="btn")
    async def Bonus(call: types.CallbackQuery):
        your_name = call.from_user.first_name
        if call.data == "btnBonus1":

            if (db.bonus_ex(call.from_user.id)):
                await call.message.answer(f'<b>⛔ | {your_name}, этот бонус уже ваш!</b>', parse_mode='html')
            else:
                if (int(db.get_balance(call.from_user.id)) > 1500):
                    db.balance_update(int(db.get_balance(call.from_user.id)) - 1500, call.from_user.first_name, call.from_user.id)
                    db.add_bonus(call.from_user.id, call.from_user.first_name)
                    await call.message.answer(f'<b>✅ | {your_name}, бонус успешно приобретен!</b>', parse_mode='html')
                else:
                    await call.message.answer(f'<b>⛔ | {your_name}, у вас недостаточно средств!</b>\n<i>(требуется 1500 флоренов)</i>', parse_mode='html')
        elif call.data == "btnBonus2":
            if (db.bonus2_ex(call.from_user.id)):
                await call.message.answer(f'<b>⛔ | {your_name}, этот бонус уже ваш!</b>', parse_mode='html')
            else:
                if (int(db.get_balance(call.from_user.id)) > 950):
                    db.balance_update(int(db.get_balance(call.from_user.id)) - 950, call.from_user.first_name, call.from_user.id)
                    db.add_bonus2(call.from_user.id, call.from_user.first_name)
                    await call.message.answer(f'<b>✅ | {your_name}, бонус успешно приобретен!</b>', parse_mode='html')
                else:
                    await call.message.answer(
                        f'<b>⛔ | {your_name}, у вас недостаточно средств!</b>\n<i>(требуется 950 флоренов)</i>',
                        parse_mode='html')
        elif call.data == "btnBonus3":
            if (db.bonus3_ex(call.from_user.id)):
                await call.message.answer(f'<b>⛔ | {your_name}, этот бонус уже ваш!</b>', parse_mode='html')
            else:
                if (int(db.get_balance(call.from_user.id)) > 10000):
                    current_datetime = int(time.time()) + minutes_to_seconds(1)
                    db.balance_update(int(db.get_balance(call.from_user.id)) - 10000, call.from_user.first_name, call.from_user.id)
                    db.add_bonus3(call.from_user.id, call.from_user.first_name, current_datetime)
                    await call.message.answer(f'<b>✅ | {your_name}, бонус успешно приобретен!</b>', parse_mode='html')
                else:
                    await call.message.answer(f'<b>⛔ | {your_name}, у вас недостаточно средств!</b>\n<i>(требуется 10000 флоренов)</i>', parse_mode='html')



    @dp.callback_query_handler(text_contains="BonusList")
    async def BonusList1(call: types.CallbackQuery):
        if call.data == "BonusList":
            await call.message.answer('<b>⭐ СПИСОК ВСЕХ ДОСТУПНЫХ БОНУСОВ: </b>\n \n'
                                 '💎 №1 <b>Вторая жизнь</b> '
                                 '\nДает возможность получать флорены, как за два фарма.\n'
                                 '<i>Стоимость: 1500 флоренов</i>'
                                 '\n\n🕊 №2 <b>Ласточка</b>'
                                 '\nСнижает время до следующего фарма на один час.\n'
                                 '<i>Стоимость: 950 флоренов</i>'                                
                                 '\n\n💮 №3 <b>Лакомка</b> '
                                 '\nКаждые 4 часа начисляет флорены на ваш баланс. (не влияет '
                                 'на основное время и равноценно обычному фарму)\n'
                                 '<i>Стоимость: 10000 флоренов</i>'
                                 '\n\n<i>‼ бонусы выдаются навсегда</i>', parse_mode='html', reply_markup=nav.mainMenu)

	#МУТЫ---------------------------------------------------------------------------------------------------------

    if (not db.user_ex2(message.from_user.id)): #проверка на присутствие пользователя в бд ct_users
    	db.add_user_mute(message.from_user.id, message.from_user.username)

    if db.mute(message.from_user.id):
    	await message.delete()


   # @dp.message_handler()
   # async def lakomka1(message: types.Message):





    #run long-polling
if __name__ == "__main__":

	executor.start_polling(dp, skip_updates=True)

#if __name__ == "__main__":
	#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)