from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Найти пропавшее Животное'), KeyboardButton (text='Наш Сайт',  callback_data="get_site")]],
    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку', selective=True)