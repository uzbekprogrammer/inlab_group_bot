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

frontend = ["""Frontendga kurs yoq dedim sizgaa"""

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

@dp.message_handler(IsGroup(), Command('address', prefixes='!#$&/'))
async def mess_addres(message: types.Message):
    await message.answer('Assalomu alaykum!\n'
                         'Manzil: Namangan Shaxri, Boburshox ko\'chasi 23 - uy\n'
                         'Mo\'ljal: Boss Milk ro\'parasida')
    await message.delete()


@dp.message_handler(IsGroup(), Command('backend', prefixes='!#$&/'))
async def mess_backend(message: types.Message):
    for i in backend:
        await message.answer(i)
    await message.delete()


@dp.message_handler(IsGroup(), Command('frontend', prefixes='!#$&/'))
async def mess_backend(message: types.Message):
    for i in frontend:
        await message.answer(i)
    await message.delete()


@dp.message_handler(IsGroup(), Command('itcourse', prefixes='!#$&/'))
async def mess_backend(message: types.Message):
    for i in all:
        await message.answer(i)
    await message.delete()


@dp.message_handler(IsGroup(), Command('courses', prefixes='!#$&/'))
async def mess_course(message: types.Message):
    for i in courses:
        await message.answer(i)
    await message.delete()

# ----------------------------------------------------------------------------------------------------------------------
# /ro oki !ro (read-only) komandalari uchun handler
# foydalanuvchini read-only ya'ni faqat o'qish rejimiga o'tkazib qo'yamiz.
@dp.message_handler(IsGroup(), Command("ro", prefixes="!#$&/"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    """
    !ro 
    !ro 5 
    !ro 5 test
    !ro test
    !ro test test test
    /ro 
    /ro 5 
    /ro 5 test
    /ro test
    """
    # 5-minutga izohsiz cheklash
    # !ro 5
    # command='!ro' time='5' comment=[]

    # 50 minutga izoh bilan cheklash
    # !ro 50 reklama uchun ban
    # command='!ro' time='50' comment=['reklama', 'uchun', 'ban']

    time = int(time)

    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik! {err.args}")
        return

    # Пишем в чат
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
                         f"Sabab: \n<b>{comment}</b>")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    # 5 sekun kutib xabarlarni o'chirib tashlaymiz
    await asyncio.sleep(1)
    await message.delete()
    await service_message.delete()

# read-only holatdan qayta tiklaymiz
@dp.message_handler(IsGroup(), Command("unro", prefixes="!#$&/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("Xabar 1 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(1)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi {member.full_name} tiklandi")

    # xabarlarni o'chiramiz
    await message.delete()
    await service_message.delete()

# Foydalanuvchini banga yuborish (guruhdan haydash)
@dp.message_handler(IsGroup(), Command("ban", prefixes="!#$&/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 1 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(1)
    await message.delete()
    await service_message.delete()

# Foydalanuvchini bandan chiqarish, foydalanuvchini guruhga qo'sha olmaymiz (o'zi qo'shilishi mumkin)
@dp.message_handler(IsGroup(), Command("unban", prefixes="!#$&/"), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} bandan chiqarildi")
    service_message = await message.reply("Xabar 1 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(1)

    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("del", prefixes="!#$&/"), AdminFilter())
async def unban_user(message: types.Message):
    # member = message.reply_to_message.from_user

    await asyncio.sleep(1)

    await message.delete()
    # await service_message.delete()
    await message.reply_to_message.delete()


@dp.message_handler(IsGroup(), Command('type', prefixes="!#$/"), AdminFilter())
async def type(message: types.Message):
    try:
        member = message.reply_to_message.from_user
    except:
        member = message.text
    # member_id = member.id
    # chat_id = message.chat.id
    command_parse = re.compile(r"(!type|/type) ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    comment = parsed.group(2)
    await message.delete()
    try:
        await message.reply_to_message.reply(comment)
    except:
        await message.answer(comment)
