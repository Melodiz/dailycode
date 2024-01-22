from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_keybord_start():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Data overview')
    keyboard_builder.button(text='Data details')
    keyboard_builder.button(text='Data transformation')
    keyboard_builder.button(text='Hypothesis checking')
    keyboard_builder.button(text='Descriptions & links')

    keyboard_builder.adjust(2, 2)

    return keyboard_builder.as_markup(resize_keyboard=True,
                                      one_time_keyboard=False,
                                      input_field_placeholder='choose the button:',
                                      selective=True)


def build_keybord_data_overview():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='show dataframes in row form')
    keyboard_builder.button(text='records of male and female transfers')
    keyboard_builder.button(text='time period covered in the data')
    keyboard_builder.button(text='mean, std, e.t.c')
    keyboard_builder.button(text='back to menu')

    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)


def build_keybord_data_details():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Distribution charts')
    keyboard_builder.button(text='Searching for correlation')
    keyboard_builder.button(text='THE PENZA ANOMALY')
    keyboard_builder.button(text='map')
    keyboard_builder.button(text='back to menu')

    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)


def build_keybord_distributions():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='income distribution')
    keyboard_builder.button(text='time distribution')
    keyboard_builder.button(text='categorisation')
    keyboard_builder.button(text='city distribution')
    keyboard_builder.button(text='back to data details')

    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)


def build_keybord_corelations():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='restaurants')
    keyboard_builder.button(text='car owners')
    keyboard_builder.button(text='medicine')
    keyboard_builder.button(text='travelling')
    keyboard_builder.button(text='back to data details')

    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)

def build_keyboard_penza():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='overview')
    keyboard_builder.button(text='categories')
    keyboard_builder.button(text='terminals')
    keyboard_builder.button(text='anomaly time')
    keyboard_builder.button(text='back to data details')

    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)

def build_data_transformation():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Data cleaning')
    keyboard_builder.button(text='Merging Dataframes')
    keyboard_builder.button(text='Edit cells')
    keyboard_builder.button(text='Enother stuff')
    keyboard_builder.button(text='back to menu')

    keyboard_builder.adjust(2, 2, 1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)


def build_check_theory():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='prepared theories')
    keyboard_builder.button(text='interactive partition')
    keyboard_builder.button(text='back to menu')

    keyboard_builder.adjust(2,1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)


def build_check_theory_manual():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Correlation between earnings and spending')
    keyboard_builder.button(text='seasonality')
    keyboard_builder.button(text='car owners corelation')

    keyboard_builder.button(text='back')

    keyboard_builder.adjust(1,2,1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)

def build_check_theory_auto():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='display list of categories')
    keyboard_builder.button(text='back')

    keyboard_builder.adjust(1,1)

    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='choose the button:',
        selective=True)
