from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

TOKEN_API = "6742857616:AAE9cbUJBzUnF0v7p9XmKelpCfTzb9mykFw"


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!')


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
