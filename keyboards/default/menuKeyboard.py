from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
Bookshelf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fan kurslarimiz"),
            KeyboardButton(text='IT kurslar')
        ],
        [
            KeyboardButton(text='Biz bilan bog\'lanish')
        ]
    ],
    resize_keyboard=True
)