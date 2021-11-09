from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from keyboards.default.menuKeyboard import Bookshelf
from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum  {message.from_user.full_name}!\n"
                         f"InLAB academy rasmiy botiga xush kelibsiz.", reply_markup=Bookshelf)
