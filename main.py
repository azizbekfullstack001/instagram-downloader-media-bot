import  logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '7526459851:AAH0FPp70mwGncEANHxgAUJpEG5nx4cZDSE'
from api import  getUrl
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler()
async  def getInstagramVideo(msg:types.Message):
    try:
        await msg.answer(f"🔍")
        await msg.reply_video(getUrl(msg.text))
    except:
        await msg.answer("iltimos video havolasini yuboring")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)