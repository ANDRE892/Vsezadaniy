from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from key.key_markup import get_1, get_2
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=f'{TELEGRAM_TOKEN}')
dp = Dispatcher(bot)

keyboard_inline = InlineKeyboardMarkup(row_width=2)
but_inline = InlineKeyboardButton('Нейросеть с текстом')
but_inline2 = InlineKeyboardButton('Нейросеть для создания фотографий')
keyboard_inline.add(but_inline, but_inline2)
async  def set_comm(bot: Bot):
    commands = [
        types.BotCommand(command='start', description='ком'),
        types.BotCommand(command='bots_text', description='Нейросеть с текстом'),
        types.BotCommand(command='bots_photo', description='Нейросеть для создания фотографий')
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('привет', reply_markup=get_1())

@dp.message_handler(lambda message: message.text=='Нейросеть с текстом')
async def Button_1_(message: types.Message):
    await  message.answer('кнопка с текстом')

@dp.message_handler(lambda message: message.text == 'следующая клавиатура')
async def Button_2_(message: types.Message):
    await  message.answer('ты на след клаве', reply_markup=get_2())

@dp.message_handler(lambda message: message.text=='Нейросеть для создания фотографий')
async def Button_3_(message: types.Message):
    await  message.answer('кнопка для создания фотографий')

@dp.message_handler(lambda message: message.text=='предыдущая клавиатура')
async def Button_4_(message: types.Message):
    await  message.answer('ты на пред клаве', reply_markup=get_1())

async def on_start(dispatcher):
    await set_comm(dispatcher.bot)
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True, on_startup= on_start)
