from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import build_data_transformation


async def data_transformation_start(message: Message, bot: Bot):
    introdaction_text = "There are many examples "\
        "of data transformation in different sections of business "\
        "analytics, but here are a couple of them with code.\n"\
        "Choose a section:"

    await message.answer(
        text=introdaction_text,
        reply_markup=build_data_transformation())


    