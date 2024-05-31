from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import TELEGRAM_TOKEN

bot = Bot(token=f'{TELEGRAM_TOKEN}')
dp = Dispatcher(bot)

# Создаем первую inline-клавиатуру
keyboard_inline = InlineKeyboardMarkup(row_width=2)
but_inline = InlineKeyboardButton('Нейросеть с текстом', callback_data='neiro_text')
but_inline2 = InlineKeyboardButton('Следующая клавиатура', callback_data='next_keyboard')
keyboard_inline.add(but_inline, but_inline2)

# Создаем вторую inline-клавиатуру
keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
but_inline3 = InlineKeyboardButton('Предыдущая клавиатура', callback_data='prev_keyboard')
but_inline4 = InlineKeyboardButton('Нейросеть для создания фотографий', callback_data='neiro_photo')
keyboard_inline_2.add(but_inline4, but_inline3)

async def set_comm(bot: Bot):
    commands = [
        types.BotCommand(command='start', description='ком'),
        types.BotCommand(command='bots_text', description='Нейросеть с текстом'),
        types.BotCommand(command='bots_photo', description='Нейросеть для создания фотографий')
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('привет', reply_markup=keyboard_inline)

@dp.callback_query_handler(lambda c: c.data == 'neiro_text')
async def process_neiro_text(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'кнопка с текстом')

@dp.callback_query_handler(lambda c: c.data == 'neiro_photo')
async def process_neiro_photo(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'кнопка для создания фотографий')

@dp.callback_query_handler(lambda c: c.data == 'next_keyboard')
async def process_next_keyboard(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Следующая клавиатура', reply_markup=keyboard_inline_2)

@dp.callback_query_handler(lambda c: c.data == 'prev_keyboard')
async def process_prev_keyboard(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Предыдущая клавиатура', reply_markup=keyboard_inline)

async def on_start(dispatcher):
    await set_comm(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)

