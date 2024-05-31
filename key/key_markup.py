from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    Button_1 = KeyboardButton('Нейросеть с текстом')
    Button_2 = KeyboardButton('следующая клавиатура ')
    keyboard.add(Button_1, Button_2)
    return keyboard

def get_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    Button_3 = KeyboardButton('Нейросеть для создания фотографий')
    Button_4 = KeyboardButton('предыдущая клавиатура')
    keyboard_2.add(Button_3, Button_4)
    return keyboard_2