from aiogram import Bot, Dispatcher
import asyncio

from core.handlers.basic import get_start

TOKEN_API = "6742857616:AAE9cbUJBzUnF0v7p9XmKelpCfTzb9mykFw"


async def start():
    bot = Bot(token=TOKEN_API)

    dp = Dispatcher()

    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
