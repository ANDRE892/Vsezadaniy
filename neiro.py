import requests
from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN, NEYRO_KEY_TEXT

API_TOKEN = 'NEYRO_KEY_TEXT'
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
API_KEY = 'TELEGRAM_TOKEN'

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("привет, я реальный пацан...")

async def get_response(message_text):
    prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 1,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "отвечай как персонаж из слово пацана, будь дерзким"
        },
        {
            "role": "user",
            "text": message_text
        }
    ]
}

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key AQVN3gcd3yAIa_q-Wc6N677Hajt7JAAbtJWCF1yk"
    }

    response = requests.post(url, headers=headers, json=prompt)
    print(response)
    result = response.json()
    print(result)
    return result['result']['alternatives'][0]['message']['text']

@dp.message_handler()
async def analize_message(message:types.Message):
    response_text = await get_response((message.text))
    await message.answer(response_text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)