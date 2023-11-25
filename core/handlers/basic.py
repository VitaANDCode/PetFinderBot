from aiogram import Bot
from aiogram.types import Message
from core.keyboards.Reply import reply_keyboard


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Представляю вашему вниманию сервис для идентификации пропавших животных.', reply_markup=reply_keyboard)

