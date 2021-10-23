from aiogram import types
from filters import AdminFilter
from loader import dp


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("courses", "Inlab o'quv markazidagi barcha kurslar"),
            types.BotCommand("address", "Bizning manzil"),
            types.BotCommand("itcourse", "IT boyicha kurslarimiz"),
            types.BotCommand("backend", "Backend kurslarimiz"),
            types.BotCommand("frontend", "Frontend kurslarimiz"),

        ]
    )
