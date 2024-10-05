import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import comands

logging.basicConfig(level=logging.INFO)

# bot = Bot(token=os.getenv("BOT_TOKEN"))
bot = Bot(token="6739109992:AAFGEIXK2knrwgLL8V2_a8r6wOdgFaMab6o")
dp = Dispatcher()


dp.include_router(comands.router)
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
