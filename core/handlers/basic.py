from aiogram import Bot
from aiogram.types import Message
from core.keyboards.Reply import reply_keyboard
from core.keyboards.Inline import site_link


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Представляю вашему вниманию сервис для идентификации пропавших животных.', reply_markup=reply_keyboard)


async def get_links(message: Message, bot : Bot):
    await bot.send_message(message.from_user.id, f'Перейти на наш сайт вы можете по ссылке ниже',reply_markup=site_link)