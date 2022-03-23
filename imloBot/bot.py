import logging
from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord

API_TOKEN = 'Your bot token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Imlo botiga xush Kelibsiz! Eslatma faqat kirill alifbosida yozing!!! Muammo bo'lsa /help")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Muammo bo'lsa https://t.me/brainbox_8 bilan bog'laning")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
