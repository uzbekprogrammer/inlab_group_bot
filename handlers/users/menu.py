from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from keyboards.default import fanKursKey, Bookshelf
from keyboards.default.itKursKey import itKurs
from loader import dp


@dp.message_handler(IsPrivate(), text='Fan kurslarimiz')
async def show_fan_kurslar(message: Message):
    await message.answer(text='Bizda quyidagi kurslar mavjud :',reply_markup=fanKursKey)


@dp.message_handler(IsPrivate(), text='IT kurslar')
async def show_it_kurs(message: Message):
    await message.answer(text="Bizda quyidagi IT kurslar mavjud: ", reply_markup=itKurs)


@dp.message_handler(IsPrivate(), text='Biz bilan bog\'lanish')
async def show_we(message: Message):
    await message.answer(text="<a href='https://t.me/AbduqodirIELTS_9'>Abduqodir Toshpo'latov</a>ga bog'laning")


@dp.message_handler(IsPrivate(), text='Orqaga 🔙')
async def asadjas(message: Message):
    await message.answer(text='Orqaga qaytildi',reply_markup=Bookshelf)
