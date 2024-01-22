from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from core.keyboards.reply import build_check_theory_manual, build_check_theory

async def build_check_mode(message: Message, bot: Bot):
    init_text = "Choose one of the two sections:\n"\
    "Interactive section\n"\
    "Prepared hypotheses section"

    await message.answer(
        text = init_text, 
        reply_markup=build_check_theory())



async def check_manual_init(message: Message, bot: Bot):
    intit_text = "There are likely to be no new graphs here. "\
        "I have already tested enough theories."
    
    await message.answer(
        text=intit_text, 
        reply_markup=build_check_theory_manual())
    

async def check_corelations_car(message: Message, bot: Bot):
    theory_intro_text = "Theory: people who own cars earn more than people who do not own cars.\n"\
        "To do this, we will compare the income of people whose transactions were transactions "\
        "related to car ownership (such as gas stations, car washes, service stations, etc.) "\
        "with the income of people without a car. We will exclude extremes for clarity."
    
    overview_text = "As a result, out of 7559 users, 3924 thousand are car owners "\
        "(well, or they paid someone for a service station). Car owners made 2_115_721 out of "\
        "3_563_529 transactions"
    
    overview_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/cars_row_dataframe.jpg')
    
    await message.answer(theory_intro_text)
    await message.answer(overview_text)
    await message.answer_photo(overview_photo)

    add_theory_text = "In addition, we will see the ratio of men and women "\
        "car drivers. I assume that men are more."
    

    gender_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/car_gender_distr.png')

    gnder_conclusion = "Thus, we can't discard this theory."
    
    await message.answer(add_theory_text)
    await message.answer_photo(gender_photo)
    await message.answer(gnder_conclusion)
    
    income_intro = "Let's see if there is a correlation between income and having a car"

    income_box = FSInputFile(
        'core/handlers/media_files/data_details/corelations/car_inc_box.png'
    )
    income_conclusion = "Thus, we can not exclude this theory as well."
    
    await message.answer(income_intro)
    await message.answer_photo(income_box)
    await message.answer(income_conclusion)


async def check_corelation_income(message: Message, bot: Bot):
    theory_init = "Our theory: The more a person earns, "\
        "the more he spends on travelling and medicine."
    
    await message.answer(theory_init)
    await message.answer('start from medicine:')

    inc_scatter_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/med_scatter_income.png'
    )
    scatter_conclusion = "The correlation is weak due to the high density near "\
        "the origin. Let’s try to make "\
    "a bar chart out of this. To do this, we will round the income, group by it, and take "\
    "the median value of spending on medicine."

    await message.answer_photo(inc_scatter_photo)
    await message.answer(scatter_conclusion)

    advanced_bar_row_text = "There is a correlation between the user's income level "\
        "and their spending on medicine, but the graph is a bit noisy due to "\
        "hospitals spending. Let's leave only pharmacies:"
    
    advanced_bar_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/med_income_bar_row.png'
    )
    advanced_barline_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/med_inc_barline.png'
    )

    conclusion_medicine = "Thus, we can't discard this theory."


    await message.answer_photo(advanced_bar_photo)
    await message.answer(advanced_bar_row_text)
    await message.answer_photo(advanced_barline_photo)
    
    await message.answer(conclusion_medicine)

    await message.answer('check trevel sector now:')

    into_text = "Let's look at the transactions related to leisure."\
        "Such as: rental of cars, railway and air transportation, hotels, etc."
    row_dataframe_text = "Thus, we received about 15 thousand "\
        "transactions, which, in fact, is not a lot"
    row_dataframe_photo = FSInputFile(
        'core/handlers/media_files/data_details/trevel/row_transactions.jpg')
    
    await message.answer(into_text)
    await message.answer(row_dataframe_text)
    await message.answer_photo(row_dataframe_photo)

     # income corelation ssector:

    inc_scatter_photo = FSInputFile(
        'core/handlers/media_files/data_details/trevel/inc_scatter.png'
    )

    scatter_conc_text = "Let's try to make the correlation more visible: "\
        "round up income and group users by it, taking the median travel expenses."
    
    inc_pro_row = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/inc_pro_row.png'
        )
    )

    inc_pro_selected = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/inc_pro_selected.png'
        )
    )

    inc_pro_gr = [
        inc_pro_row, 
        inc_pro_selected
    ]

    conclusion_trevel = "Thus, we can not exclude this theory as well."


    await message.answer_photo(inc_scatter_photo)
    await message.answer(scatter_conc_text)
    await message.answer_media_group(inc_pro_gr)
    await message.answer(conclusion_trevel)


async def check_seasonality(message: Message, bot: Bot):
    hypotheses_inint = "Our theory: There is a certain seasonality "\
        "to when people spend money on travel and medicine. For example, "\
        "in autumn and spring, spending on pharmacies increases, and in summer "\
        "and winter, spending on trips increases. Clarification: we can not "\
        "unambiguously determine the date of a transaction, as the date of our "\
        "transaction is indicated in days passed from some unix day, which we do not know."
    
    """medicine"""

    intro_row_text = "We got the following date set:"
    intro_photo_row = FSInputFile(
        'core/handlers/media_files/data_details/corelations/medicine_row.jpg'
    )
    week_text = "Let's display the data split by week, since a displaying "\
        "day is not representative."
    
    pro_text = "Hmm, total spending across all medical categories looks uninformative, "\
        "let's break this graph down into a few "
    
    scatter_plot = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/corelations/med_scatter_week.png'
        )
    )
    line_pro = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
           'core/handlers/media_files/data_details/corelations/medicine_line_pro.png' 
        )
    )
    line_graph = FSInputFile(
        'core/handlers/media_files/data_details/corelations/med_line_week.png'
    )
    
    mg_pro = [line_pro, scatter_plot]

    conclusion_medicine = "Thus, we can't discard this theory."

    await message.answer(hypotheses_inint)
    await message.answer(intro_row_text)
    await message.answer_photo(intro_photo_row)

    await message.answer(week_text)
    await message.answer_photo(line_graph)
    
    await message.answer(pro_text)
    await message.answer_media_group(mg_pro)
    await message.answer(conclusion_medicine)

    """trevel"""

    into_text = "Let's look at the transactions related to leisure."\
        "Such as: rental of cars, railway and air transportation, hotels, etc."
    row_dataframe_text = "Thus, we received about 15 thousand "\
        "transactions, which, in fact, is not a lot"
    row_dataframe_photo = FSInputFile(
        'core/handlers/media_files/data_details/trevel/row_transactions.jpg'
    )

    await message.answer(into_text)
    await message.answer(row_dataframe_text)
    await message.answer_photo(row_dataframe_photo)

    weeks_intro_text = "We group expenses by week and then look at which "\
        "week has how much spent on travelling, in order to see the seasonality."

    weeks_intro_photo_def_photo = FSInputFile(
        'core/handlers/media_files/data_details/trevel/weeks_bar_row_defualt.png'
    )
    weeks_def_conclusion_text = "We should group categories of expenses, "\
        "and, finally, translate them into English."
    
    weeks_gr_row_def_photo = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
        'core/handlers/media_files/data_details/trevel/weeks_bar_gr_row.png'
        )
    )
    weeks_gr_sel_row_photo = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
        'core/handlers/media_files/data_details/trevel/weeks_bar_gr_selected.png'
        )
    )
    gr_weeks_gr_def = [weeks_gr_row_def_photo,
                       weeks_gr_sel_row_photo]
    
    weeks_gr_def_conc_text = "Let's now construct a linear graph and increase "\
        "the step: now we will group by 2 weeks."

    
    await message.answer(weeks_intro_text)
    await message.answer_photo(weeks_intro_photo_def_photo)
    await message.answer(weeks_def_conclusion_text)
    await message.answer_media_group(gr_weeks_gr_def)
    await message.answer(weeks_gr_def_conc_text)


    adv_line_row_photo = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/adv_line_row.png'
        )
    )

    adv_line_part_photo = InputMediaPhoto(
    type='photo', 
    media=FSInputFile(
        'core/handlers/media_files/data_details/trevel/adv_line_part.png'
        )
    )
    adv_line_fun_photo = InputMediaPhoto(
        type='photo',
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/week_dist_fun_line.png'
        )
    )

    adv_gr = [adv_line_row_photo,
              adv_line_part_photo,
              adv_line_fun_photo]
    
    conclusion_trevel = "Thus, we can not exclude this theory as well."
    
    
    await message.answer_media_group(adv_gr)
    await message.answer(conclusion_trevel)

