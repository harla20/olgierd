from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



    #список бонусов
mainMenu = InlineKeyboardMarkup(row_width=1)
btnBonus1 = InlineKeyboardButton(text="Купить 'Вторая жизнь'", callback_data="btnBonus1")
btnBonus2 = InlineKeyboardButton(text="Купить 'Ласточка'", callback_data="btnBonus2")
btnBonus3 = InlineKeyboardButton(text="Купить 'Лакомка'", callback_data="btnBonus3")
    #вызов бонусов
Bonuses = InlineKeyboardMarkup(row_width=1)
BonusList = InlineKeyboardButton(text="Улучшить ферму", callback_data="BonusList")


mainMenu.insert(btnBonus1)
mainMenu.insert(btnBonus2)
mainMenu.insert(btnBonus3)
Bonuses.insert(BonusList)

