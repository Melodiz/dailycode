from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from core.keyboards.reply import build_check_theory_auto


async def check_auto_init(message: Message, bot: Bot):
    intit_text = "You will be able to verify your theories "\
        "by basing on numerous representative graphs for any "\
        "category you can choose using inline buttons."
    
    await message.answer(
        text=intit_text, 
        reply_markup=build_check_theory_auto())