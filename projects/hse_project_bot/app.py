from aiogram import Bot, Dispatcher
from aiogram.types import message, ContentType
import asyncio
import logging
from core.handlers.data_overiew import *
from core.handlers.data_details import *
from core.handlers.dt_init import data_transformation_start
from core.handlers.dt_clean import dt_data_cleaning
from core.handlers.dt_cells import dt_edit_cells
from core.handlers.dt_merge import dt_merging_dataframes
from core.handlers.dt_stuff import dt_enother_stuff
from core.handlers.check_theory_manual import *
from core.handlers.check_theory_auto import *
from core.handlers.descriptions import description_init
from core.settings import settings
from aiogram.filters import Command
from aiogram import F
from core.utils.commands import set_commands




BOT_USERNAME = '@hse_project_data_analys_bot'


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot has been started!')


async def end_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id,  text='Bot has been stoped!')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    # casual start and shutdown bot messages to admin's pm
    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)

    # dp.message.register(get_photo, F.photo)
    # base command:
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_start, F.text == 'back to menu')


    """Data Overview"""
    dp.message.register(data_overview, F.text == 'Data overview'
                        )
    dp.message.register(do_show_row_data, F.text =='show dataframes in row form')
    dp.message.register(do_genders_easy_plot, F.text =='records of male and female transfers')
    dp.message.register(do_time_period, F.text == 'time period covered in the data')
    dp.message.register(do_mean_std_box, F.text == 'mean, std, e.t.c')


    """Data Details"""
    dp.message.register(data_details, F.text == 'Data details')
    
    # Distribution charts
    dp.message.register(dd_distribution_charts, F.text == 'Distribution charts')

    dp.message.register(dd_distr_income, F.text == 'income distribution')
    dp.message.register(dd_distr_time, F.text == 'time distribution')
    dp.message.register(dd_distr_catigorazation, F.text == 'categorisation')
    dp.message.register(dd_distr_city, F.text == 'city distribution')


    # penza anomaly button menu
    dp.message.register(penza_anomly_start, F.text == 'THE PENZA ANOMALY')

    dp.message.register(penza_overview, F.text == 'overview')
    dp.message.register(penza_categories, F.text == 'categories')
    dp.message.register(penza_terminals, F.text == 'terminals')
    dp.message.register(penza_time_distr, F.text == 'anomaly time')


    # corelations
    dp.message.register(start_correlations, F.text == 'Searching for correlation')
    dp.message.register(data_details, F.text == 'back to data details')

    dp.message.register(dd_restaurants_cor, F.text == 'restaurants')
    dp.message.register(cor_car_owners, F.text == 'car owners')
    dp.message.register(medicine_cor, F.text == 'medicine')
    dp.message.register(trevelling, F.text == 'travelling')

    # map
    dp.message.register(dd_map, F.text == 'map')

    """Data transformation"""
    dp.message.register(data_transformation_start, F.text == 'Data transformation')

    dp.message.register(dt_data_cleaning, F.text == 'Data cleaning')    
    dp.message.register(dt_merging_dataframes, F.text == 'Merging Dataframes')
    dp.message.register(dt_edit_cells, F.text == 'Edit cells')
    dp.message.register(dt_enother_stuff, F.text == 'Enother stuff')


    """Check theory"""
    
    """prepared"""
    dp.message.register(build_check_mode, F.text == 'Hypothesis checking')
    dp.message.register(build_check_mode, F.text == 'back')

    dp.message.register(check_manual_init, F.text == 'prepared theories')
    # dp.message.register(check_auto_init, F.text == 'interactive partition')

    dp.message.register(check_corelations_car, F.text == 'car owners corelation')
    dp.message.register(
        check_corelation_income, 
        F.text == 'Correlation between earnings and spending')
    dp.message.register(check_seasonality, F.text == 'seasonality')

    """interactive"""
    dp.message.register(dd_map, F.text == 'interactive partition')

    """description"""
    dp.message.register(description_init, F.text == 'Descriptions & links')


    # casual bot logic
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    print('Staring bot...')
    asyncio.run(start())
