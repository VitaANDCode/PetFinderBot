from aiogram import Bot
from aiogram.types import Message
from core.keyboards.Inline import site_link
import datetime

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,f'Привет, {message.from_user.first_name}! Представляю вашему вниманию сервис для идентификации пропавших животных.',reply_markup= site_link)
    await get_info(message, bot)

# async def get_start(message: Message, bot: Bot):
#     await bot.send_message(message.from_user.id,f'Привет, {message.from_user.first_name}! Представляю вашему вниманию сервис для идентификации пропавших животных.')
#     await get_info(message, bot)


async def get_site(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Перейти на наш сайт вы можете по ссылке ниже', reply_markup=site_link)
    await get_info(message, bot)


async def search_pet(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Отправьте фото вашего питомца!')


async def load_photo(message: Message):
    if message.content_type == 'photo':
        await message.bot.download(message.photo[-1], r"C:\Users\User\Desktop\PetFinderBot\core\handlers\Photo\\" + ''.join(str(datetime.datetime.now()).split(':')) + ".png")












async def get_info(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Список команд:\n/search - поиск питомца\n/site - переход на наш сайт\n/info - список команд')
