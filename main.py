import  logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType

API_TOKEN = 'Yout Telegram bot token here'
# Configure logging

logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
sukinish =["eshak",'mol','axmoq']

@dp.message_handler(text=sukinish)
async  def Sukinish(msg:types.Message):
    await  msg.answer(f"so'kinma {msg.from_user.username}")

@dp.message_handler(content_types=ContentType.STICKER)
async  def info(msg:types.Message):
    await msg.delete()
    await  msg.answer("iltimos stiker yubormang!!!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
