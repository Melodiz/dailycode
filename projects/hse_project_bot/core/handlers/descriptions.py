from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from core.keyboards.reply import *

async def description_init(message: Message, bot: Bot):
    description_text = "The Telegram bot is a demo project "\
        "prepared for the Higher School of Economics by the "\
        "first-year student Ivan Novosad.\n It presents some business "\
        "analytics of the data obtained at the Sber Hackathon.This "\
        "is the closest possible imitation of real-life transactions(or "\
        "that’s real transactions, I have no confirmed information) as they "\
        "are proposed to be used to train the models. \nThe total weight of the "\
        "files in CSV format is 300 megabytes. \nFor more information about the "\
        "files, see the overview section. Special attention should be paid to "\
        "the parameter trans_time in the transactions file. These are data "\
        "in the format day / time, where day is the day past from a certain "\
        "point of reference (the first transaction in the file) and time is local time."
    
    link_git = ''
    # link_streamlit = ''
    links = f"sources:{link_git}"

    await message.answer(text = description_text)
    await message.answer(link_git)