from aiogram import Bot
from aiogram.types import Message
from core.keyboards.Inline import site_link


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,f'Привет, {message.from_user.first_name}! Представляю вашему вниманию сервис для идентификации пропавших животных.')
    await get_info(message, bot)


async def get_site(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Перейти на наш сайт вы можете по ссылке ниже', reply_markup=site_link)
    await get_info(message, bot)


async def search_pet(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Отправьте фото вашего питомца!')


async def get_info(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Список команд:\n/search - поиск питомца\n/site - переход на наш сайт\n/info - список команд')
