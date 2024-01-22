from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def display_list_of_categories():
    keboard_builder = InlineKeyboardBuilder()

    keboard_builder.button(
        text='', 
        callback_data='')