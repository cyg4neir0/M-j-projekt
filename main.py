from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(msg: types.Message):
    await msg.answer("Bot działa na Koyeb! 🚀")

if __name__ == "__main__":
    executor.start_polling(dp)
