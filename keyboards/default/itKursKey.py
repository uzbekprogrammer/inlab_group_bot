from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

itKurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Frontend "),
            KeyboardButton(text='Backend')
        ],
        [
            KeyboardButton(text='Mobile')
        ],
        [
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)