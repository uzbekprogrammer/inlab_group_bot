from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
fanKursKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ona tili va adabiyoti"),
            KeyboardButton(text="Tarix")
        ],
        [
            KeyboardButton(text='Biologiya (uzb)'),
            KeyboardButton(text="Биология (рус)")
        ],
        [
            KeyboardButton(text="Kimyo (uzb)"),
            KeyboardButton(text="Химия (рус)")
        ],
        [
            KeyboardButton(text="Geografiya"),
            KeyboardButton(text="Mental arifmetika")
        ],
        [
            KeyboardButton(text="Matematika"),
            KeyboardButton(text="Fizika")
        ],
        [
            KeyboardButton(text="Ingliz tili"),
            KeyboardButton(text='Rus tili')
        ],
        [
            KeyboardButton(text="Arab tili"),
            KeyboardButton(text='Koreys tili')
        ],
        [
            KeyboardButton(text="Nemis tili"),
            KeyboardButton(text="Prezident maktabiga tayyrlov")
        ],
        [
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)