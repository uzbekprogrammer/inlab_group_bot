import asyncio
import datetime
import re
import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import IsGroup, AdminFilter
from loader import dp, bot
backend = ["Assalomu alaykum! \n\n"

        "Backend development kursi \n"
        "Narxi: 400 ming so'm\n"
        "Davomiyligi: 6 oy\n\n"
        
        "Kurs davomida o'ragtiladigan texnalogiyalar: \n"
        "Foundation\n"
        "Python 🐍\n"
        "Flask\n"
        "Django\n\n"
        
        "Kurs so'ngigacha 3 ta loyiha tugatiladi 💻",
         ]

all=["O'quv markazimizda quyidagi kurslar orqali sizda Java, Python, Javascript va boshqa o'ndan ortiq yo'nalishlardan birida mutaxassis bo'lish imkoni mavjud: \n\n"

    "▪️IT KIDS \n"
    "- Mobil o'yinlar va veb sahifalar yaratish \n"
    "- IT English \n"
    "- Mnemonika darslari \n\n"
    
    "▪️ Web Dasturlash \n"
    "-Web Design \n"
    "-Frontend \n"
    "-Backend\n\n"
    
    "▪️ Mobil Dasturlash\n "
    "-Java, Kotlin\n "
    "-Android Basic\n"
    "-Android advanced\n"
    ]

frontend = [

]

courses=["""INLAB Academy o'z ishini boshladi va sizlarga o'z kurslarini taklif qiladi.

✅Mental arifmetika       ✅Ingliz tili
✅Ona tili va adabiyoti   ✅Rus tili
✅Biologiya (uzb,рус)    ✅Koreys til
✅Kimyo (uzb,рус)         ✅Nemis tili
✅Matematika                 ✅Fizika
✅Geografiya                   ✅Tarix     
✅Frontend                      ✅Mobile
✅Backend

Biz bilan zamonaviy bilmlar egasi bol.

Nega aynan bizni tanlashingiz kerak.🤷🏻
1.Malakali o'qituvchilar👨‍💼
2.Zamonaviy o'quv xonalari🏢
3.Supper chegirmalar🎁
va sizlarni biz bilan yorqin kelajak kutmoqda.💯

I.📋 FANLAR VA TILLAR BO'YICHA STANDART KURS NARXI - 150 ming so'm

II. 💻 DARSTURLASH KURSLARI  - 400 mingdan boshlab 
""",
         """Assalomu alaykum! 

IT kids
Narxi: 300 ming so'm 
Davomiyligi: 3 oy

Frontend development 
Narxi: 400 ming so'm
Davomiyligi: 6 oy

Backend development 
Narxi: 400 ming so'm
Davomiyligi: 6 oy

Mobile development
Narxi: 500 ming so'm
Davomiyligi: 8 oy

Ilk o'quvchilar uchun har bir kurslarga 3 oy muddatda 50 ming so'mdan chegirma mavjud!"""
]

@dp.message_handler(IsGroup(), Command('address', prefixes='!#$&'))
async def mess_addres(message: types.Message):
    await message.reply('Assalomu alaykum!\n'
                         'Manzil: Namangan Shaxri, Boburshox ko\'chasi 23 - uy\n'
                         'Mo\'ljal: Boss Milk ro\'parasida')


@dp.message_handler(IsGroup(), Command('backend', prefixes='!#$&'))
async def mess_backend(message: types.Message):
    for i in backend:
        await message.reply(i)


@dp.message_handler(IsGroup(), Command('frontend', prefixes='!#$&'))
async def mess_backend(message: types.Message):
    for i in frontend:
        await message.reply(i)


@dp.message_handler(IsGroup(), Command('itcourse', prefixes='!#$&'))
async def mess_backend(message: types.Message):
    for i in all:
        await message.reply(i)


@dp.message_handler(IsGroup(), Command('courses', prefixes='!#$&'))
async def mess_course(message: types.Message):
    for i in courses:
        await message.reply(i)


