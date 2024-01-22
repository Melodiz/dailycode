from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from core.keyboards.reply import *


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f'{message.from_user.first_name}, select the section of interest using the button menu',
                         reply_markup=build_keybord_start())


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Nice, I get your picture and save it :)')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def data_overview(message: Message, bot: Bot):
    await message.answer(
        text='Use the button menu to select a section', 
        reply_markup=build_keybord_data_overview())


async def do_show_row_data(message: Message, bot: Bot):

    answer_text = 'First of all, we have 4 csv files with data:\n'

    photo_mcc_codes_row = FSInputFile(
        'core/handlers/media_files/data_overview/mcc_codes_row.png')
    photo_transactions_row = FSInputFile(
        'core/handlers/media_files/data_overview/transactions_row.png')
    photo_trans_type_row = FSInputFile(
        'core/handlers/media_files/data_overview/trans_type_row.png')
    photo_genders_row = FSInputFile(
        'core/handlers/media_files/data_overview/genders_row.png')

    await message.answer(answer_text)
    await message.answer_photo(photo=photo_transactions_row,
                               caption='file with transactions')
    await message.answer_photo(photo=photo_mcc_codes_row,
                               caption='file with all mcc_codes')
    await message.answer_photo(photo=photo_trans_type_row,
                               caption='file with transactions types')
    await message.answer_photo(photo=photo_genders_row,
                               caption='file with genders of clients named "train.csv')


async def do_genders_easy_plot(message: Message, bot: Bot):

    photo_genders_count = FSInputFile(
        'core/handlers/media_files/data_overview/male_female_count.jpg')

    await message.answer_photo(photo=photo_genders_count,
                               caption='How many records are there of male and female transfers')


async def do_time_period(message: Message, bot: Bot):
    answer_text = 'transaction time data is recorded in the form of how many'\
        'days have passed since the countdown date, but the time is local time '

    Adjustment_Spending_rate = FSInputFile(
        'core/handlers/media_files/data_overview/Adjustment_Spending_rate.jpg')
    Row_spending_rate = FSInputFile(
        'core/handlers/media_files/data_overview/Spending_rate.jpg'
    )

    await message.answer(answer_text)
    await message.answer_photo(photo=Row_spending_rate, caption='Row spending rate')
    await message.answer_photo(photo=Adjustment_Spending_rate, caption='Adjustment spending rate')
    await message.answer("conclusion: our data mainly contain information"
                         "on people's spending over a period of 400-450 days")


async def do_mean_std_box(message: Message, bot: Bot):
    answer_text = 'Some details on transactions, using box plots:'

    mean_spendings = FSInputFile(
        'core/handlers/media_files/data_overview/AVG_spendings_men_and_womends.jpg')
    box_plot_men_spendings = FSInputFile(
        'core/handlers/media_files/data_overview/Box_plot_men_spendings.jpg')
    adjustment_spendings_rate = FSInputFile(
        'core/handlers/media_files/data_overview/Adjusted_box_plot.jpg')

    await message.answer(answer_text)
    await message.answer_photo(photo=mean_spendings, caption='AVG_spendings')
    await message.answer_photo(photo=box_plot_men_spendings, caption="Box plot of men's spendigns")
    await message.answer_photo(photo=adjustment_spendings_rate, caption="Adjusted data about men's spendings")


