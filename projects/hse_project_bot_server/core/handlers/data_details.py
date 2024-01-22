from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto
from core.keyboards.reply import *
from time import sleep



async def data_details(message: Message, bot: Bot):
    await message.answer(
        text='Use the button menu to select a section', 
        reply_markup=build_keybord_data_details())


async def dd_distribution_charts(message: Message, bot: Bot):
    await message.answer(text='Select the section:',
                         reply_markup=build_keybord_distributions())


async def dd_distr_income(message: Message, bot: Bot):
    answer_text = 'the sum of all expenses for the whole period, for each user (row)'

    p_merge = FSInputFile(
        'core/handlers/media_files/data_details/Distr/distibution_merge_s.jpg')
    p_women_s = FSInputFile(
        'core/handlers/media_files/data_details/Distr/distibutions_women_s.jpg')
    p_mens_s = FSInputFile(
        'core/handlers/media_files/data_details/Distr/distribution_mens_s.jpg')

    await message.answer(text=answer_text)
    await message.answer_photo(photo=p_mens_s)
    await message.answer_photo(photo=p_women_s)
    await message.answer_photo(photo=p_merge)


async def dd_distr_time(message: Message, bot: Bot):
    answer_text = 'what time of day people are more likely to make transactions'

    pmen_sum = InputMediaPhoto(type='photo',
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/dist_men_time_sum.jpg'))

    pwomen_sum = InputMediaPhoto(type='photo',
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/dist_women_time_sum.jpg'))
    
    pmen_count = InputMediaPhoto(type='photo',
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/dist_men_time_count.jpg'))
    
    pwomen_count = InputMediaPhoto(type='photo',
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/dist_women_time_count.jpg'))
    
    gr_men = [pmen_sum, pmen_count]
    gr_women = [pwomen_sum, pwomen_count]

    await message.answer(text=answer_text)
    await message.answer_media_group(gr_men)
    await message.answer_media_group(gr_women)

    some_text = "Something strange around 12 o'clock, "\
        "maybe it's automated transactions. That's a theory worth testing later "

    await message.answer(some_text)


async def dd_distr_catigorazation(message: Message, bot: Bot):

    answer_text = 'get statistics on the 10 most popular expenses of men and women'

    pmen_def = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/bar_men_cat_def.jpg'
                               ))
    pmen_row = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/bar_men_cat_cor.jpg'
                               ))
    pwomen_def = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/bar_women_cat_def.jpg'
                               ))
    pwomen_row = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/bar_women_cat_cor.jpg'
                               ))
    
    mg_defult = [pmen_def, pwomen_def]
    mg_row = [pmen_row, pwomen_row]

    await message.answer(text=answer_text)
    await message.answer_media_group(mg_row)

    await message.answer(text="It is hard to comprehend the overall"\
            "situation given the overwhelming bias in the first two categories."\
            "Therefore, we should exclude those categories.")
    await message.answer_media_group(mg_defult)


async def dd_distr_city(message: Message, bot: Bot):
    answer_text = 'box plot by transaction. Distribution by city. Extremes outside the picture'

    p_men_distr = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/city_disrt_men.jpg'))
    p_women_distr = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/Distr/city_distr_women.jpg'))

    await message.answer(text=answer_text)
    await message.answer_media_group([p_men_distr, p_women_distr])

    joke_photo = FSInputFile('core/handlers/media_files/data_details/Distr/penza_maddonna.jpg')
    joke_text = "While researching the date set, discovered a woman who was"\
                "able to spend 262 million rubles in a year in Penza. HOW? BOUGHT PENZA?"
    
    await message.answer(text=joke_text)
    await message.answer_photo(joke_photo)

    stiker_file = FSInputFile('core/handlers/media_files/data_details/Distr/joke_sticker.mp4')

    await message.answer_video(video=stiker_file)




async def start_correlations(message: Message, bot: Bot):
    await message.answer(
        text='Use the button menu to select a section', 
        reply_markup=build_keybord_corelations())


async def dd_restaurants_cor(message: Message, bot: Bot):
    booger_AIDS = "Since the average or median spend is irrelevant,"\
         "let's display a graph of the sum of transactions"
    booger_AIDS_copy = FSInputFile(
        'core/handlers/media_files/data_details/corelations/rest_time_disrt_bar.jpg')

    await message.answer(booger_AIDS)
    await message.answer_photo(photo=booger_AIDS_copy)

    AIDS_booger = "find out what is the ratio between "\
        "transfers and payment by terminal in restaurants"
    
    AIDS_booger_copy = InputMediaPhoto(type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/corelations/pie_rest_terms_tranf.jpg'))
    
    AIDS_booger_copy_1 = InputMediaPhoto(type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/corelations/rest_terms_transf_bar.jpg'))
    
    AIDS_booger_final_copy = [AIDS_booger_copy_1, AIDS_booger_copy]

    await message.answer(AIDS_booger)
    await message.answer_media_group(AIDS_booger_final_copy)

    AIDS_booger_new = "Some statistics about different cities"
    AIDS_booger_new_copy = FSInputFile(
        'core/handlers/media_files/data_details/corelations/rest_box_city.jpg')

    # The name of the variables is a reference to Rick and Morty.
    await message.answer(AIDS_booger_new)
    await message.answer_photo(AIDS_booger_new_copy)



"""PENZA ANOMELY"""

    
async def penza_anomly_start(message: Message, bot: Bot):
    text = "While researching the data, I found a woman in the "\
        "data who somehow managed to spend 262 million roubles in "\
        "5 months.... IN PENZA... I was curious about what and how, "\
        "so I made a whole section about her."
    
    await message.answer(text = text, reply_markup=build_keyboard_penza())


async def penza_overview(message: Message, bot: Bot):
    intoradaction_income = "For comparison, I decided to display the median"\
        " expenditure of a Penza resident, but it just doesn't show up (152,000 rub)"
    
    photo_bar_income = FSInputFile(
        'core/handlers/media_files/data_details/penza/penza_over_income_spend.jpg')

    await message.answer(text = intoradaction_income)
    await message.answer_photo(photo=photo_bar_income)

    await message.answer('Just in case: all transactions '\
                         'of this user are registered in Penza.')
    
    month_text = "Let's see for what period and in what amount transactions were made"
    photo_month_bar = FSInputFile(
        'core/handlers/media_files/data_details/penza/month_bar.jpg')

    await message.answer(month_text)
    await message.answer_photo(photo=photo_month_bar)

    hist_text = "Hmmm, maybe most of the transactions were completely on any one day?"\
    "It could have been the day she bought Penza, for example. Let's build a histogram "\
    "with the sum of transactions by day"\
    "For the readability of the histogram, let's consider only month 4"

    hist_photo = FSInputFile(
        'core/handlers/media_files/data_details/penza/distr_four_mounth.jpg')
    
    hist_conlusion = "Conclusion: no, it wasn't one big transaction "\
    "on any given day, the distribution is roughly uniform"

    await message.answer(hist_text)
    await message.answer_photo(photo=hist_photo)
    await message.answer(hist_conlusion)


async def penza_categories(message: Message, bot: Bot):
    intro_text = "Let's find out what she spent her money on and where she got it from."

    spend_photo = InputMediaPhoto(type='photo', 
        media= FSInputFile('core/handlers/media_files/data_details/penza/penza_cat_spend.jpg'))
    income_photo = InputMediaPhoto(type = 'photo', 
        media=FSInputFile('core/handlers/media_files/data_details/penza/penza_over_income_spend.jpg'))
    
    bar_gr = [spend_photo, income_photo]

    await message.answer(intro_text)
    await message.answer_media_group(media=bar_gr)

    conlusion = "So, we won't get anything interesting out of the categories,"\
    " let's look at which ATMs and what time she withdrew the money from"

    await message.answer(text=conlusion)


async def penza_terminals(message: Message, bot: Bot):
    intro_text = "Let's find out which terminals she used to "\
        "withdraw millions in Penza. Might be something interesting"
    
    bar_photo = FSInputFile('core/handlers/media_files/data_details/penza/penza_term_bar.jpg')

    await message.answer(text = intro_text)
    await message.answer_photo(bar_photo)

    conlusion_text = "Conclusion: nothing particularly interesting,"\
    " but there are ATMs in Penza with 20 million roubles in them."

    await message.answer(text=conlusion_text)


async def penza_time_distr(message: Message, bot: Bot):
    intro_text = "Let's see at what time the money is received and debited "\
    "from the account. Maybe she withdraws the money deep into the night, "\
        "in the silence of the night, away from the eyes of witnesses."
    
    main_photo = FSInputFile('core/handlers/media_files/data_details/penza/time_distr.jpg')

    conclusion_text = "No, nothing noteworthy. Except that money is debited and received "\
        "at the same time of day. In the end, it turned out to be a rather boring anomaly. "\
            "But our job here is just to draw graphs, isn't it?"
    
    await message.answer(intro_text)
    await message.answer_photo(main_photo)
    await message.answer(conclusion_text)

    joke_file = FSInputFile('core/handlers/media_files/data_details/penza/joke.png')

    await message.answer_sticker(sticker=joke_file)



async def cor_car_owners(message: Message, bot: Bot):
    intro_text = "Let's compare the costs of car owners and those "\
        "who don't have a car. We will guess who has a car and who does "\
        "not by the presence of transactions characteristic for car owners, "\
        "such as payment for car service or petrol stations."

    
    overview_text = "As a result, out of 7559 users, 3924 thousand are car owners "\
        "(well, or they paid someone for a service station). Car owners made 2_115_721 out of "\
        "3_563_529 transactions"
    
    overview_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/cars_row_dataframe.jpg'
    )
    await message.answer(intro_text)
    await message.answer(overview_text)
    await message.answer_photo(overview_photo)


    gender_intro_text = "Let's look at the ratio of male to female motorists"
    
    gender_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/car_gender_distr.png')

    gnder_conclusion = "Conclusion, there is no clear correlation, this difference can be "\
        "attributed to a slight advantage of men over women in the number of represented users"

    await message.answer(gender_intro_text)
    await message.answer_photo(gender_photo)
    await message.answer(gnder_conclusion)

    income_intro = "Let's see if there is a correlation between income and having a car"

    income_box = FSInputFile(
        'core/handlers/media_files/data_details/corelations/car_inc_box.png'
    )
    income_conclusion = "Thus we can see a noticeable "\
        "correlation between earnings and having a car"
    
    await message.answer(income_intro)
    await message.answer_photo(income_box)
    await message.answer(income_conclusion)

    end_text = "I could make a graph of the dependence between the amount of spending"\
        "on cars and total spending for example, it would make a nice scatter plot, but"\
        " I spent too much time on this project, and I hope the project turned out "\
        "well without it, right?"
    joke_text = "I can offer memes instead"
    joke_file_1 = InputMediaPhoto(type='photo', 
        media=FSInputFile('core/handlers/media_files/data_details/corelations/aust_joke_1.png'))
    joke_file_2 = InputMediaPhoto(type='photo', 
        media=FSInputFile('core/handlers/media_files/data_details/corelations/aust_joke_2.jpg'))
    joke_group = [joke_file_1, joke_file_2]

    await message.answer(end_text)
    await message.answer(joke_text)
    await message.answer_media_group(joke_group)


async def medicine_cor(message: Message, bot: Bot):
    intro_text = "Let's take a look at when people commit "\
        "to medical spending. Maybe there's a seasonality there "
    
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

    week_conclusion_text = "Based on this, it is possible to make an assumption about "\
        "the approximate time of occurrence of autumn and spring - periods when many "\
        "people get sick with SARS."

    await message.answer(intro_text)
    await message.answer(intro_row_text)
    await message.answer_photo(intro_photo_row)

    await message.answer(week_text)
    await message.answer_photo(line_graph)
    
    await message.answer(pro_text)
    await message.answer_media_group(mg_pro)
    await message.answer(week_conclusion_text)

    inc_intro = "Let's look at the correlation between income and spending on medicine:"

    inc_scatter_photo = FSInputFile(
        'core/handlers/media_files/data_details/corelations/med_scatter_income.png'
    )
    scatter_conclusion = "The correlation is weak due to the high density near "\
        "the origin. Let’s try to make "\
    "a bar chart out of this. To do this, we will round the income, group by it, and take "\
    "the median value of spending on medicine."

    await message.answer(inc_intro)
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

    conclusion = "Yes, there is a correlation between a person's income and "\
    "their spending on medicine. The more a person earns, the more likely they "\
    "spend on medicine. Another interesting observation is that women spend more "\
    "on medicine than men on average."


    await message.answer_photo(advanced_bar_photo)
    await message.answer(advanced_bar_row_text)
    await message.answer_photo(advanced_barline_photo)
    
    await message.answer(conclusion)


async def trevelling(message: Message, bot: Bot):

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
    
    adv_conc_text = "Conclusion: a slight tendency towards seasonal "\
        "vacation can be traced, but it is not so obvious."
    
    
    await message.answer_media_group(adv_gr)
    await message.answer(adv_conc_text)

    # income corelation ssector:

    inc_intro = "Let's try to find a correlation between income and travel expenses:"

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

    inc_pro_conc_text = "Conclusion: there is a correlation between income "\
        "and travel expenses, but it is not as pronounced as expected."


    await message.answer(inc_intro)
    await message.answer_photo(inc_scatter_photo)
    await message.answer(scatter_conc_text)
    await message.answer_media_group(inc_pro_gr)
    await message.answer(inc_pro_conc_text)

    # city distr sector:
    city_cat_text = "Let's see what contribution different cities made to "\
        "the distribution of travel expenses by weeks"
    
    city_cat_row_photo = FSInputFile(
        'core/handlers/media_files/data_details/trevel/city_cat_row.png'
    )

    city_cat_conc_text = "Conclusion: in all cities spend almost the same "\
        "amount on travel, but in Kazan and Moscow spend a little more."

    city_intro_text  = "Let's look at the statistics for cities. "\
        "First we will find out who spends money on trips and when, "\
        "maybe the seasonality of different cities is different."

    city_line_row = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/city_line_row.png'
        )
    )
    city_line_similar = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/city_line_selected.png'
        ),
        caption='Similar seasons'
    )
    city_line_diff = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_details/trevel/city_line_diff.png'
        ), 
        caption='Different seasons'
    )

    city_line_gr = [
        city_line_row,
        city_line_similar,
        city_line_diff
    ]

    city_line_conc = "Conclusion: different cities indeed have different "\
        "seasons of travel spending, but there are also cities with "\
        "very similar seasonality."
    
    city_box_text = "Finally, let's compare travel expenses in different cities."

    city_box_photo = FSInputFile(
        'core/handlers/media_files/data_details/trevel/city_box_plot.png'
    )

    city_box_conc = "Conclusion: residents of different cities spend different "\
        "amounts of money on travel. Some spend more, some less, some may spend very "\
        "little, some may spend a lot if they spend anything at all, and so on."


    await message.answer(city_cat_text)
    await message.answer_photo(city_cat_row_photo)
    await message.answer(city_cat_conc_text)

    await message.answer(city_intro_text)
    await message.answer_media_group(city_line_gr)
    await message.answer(city_line_conc)

    await message.answer(city_box_text)
    await message.answer_photo(city_box_photo)
    await message.answer(city_box_conc)

    joke_file = FSInputFile(
        'core/handlers/media_files/data_details/trevel/mario_joke.png'
    )
    joke_text = "Read it all, please. I've tried my best"

    await message.answer_photo(joke_file, caption=joke_text)


async def dd_map(message: Message, bot: Bot):

    joke_file_1 = FSInputFile(
        'core/handlers/media_files/joke_missed_sections.jpeg')
    
    joke_file_2 = FSInputFile(
        'core/handlers/media_files/joke_dicap_catch.jpeg'
    )

    await message.answer_photo(joke_file_1)

    # Wait a couple of seconds to reach the peak of comedy
    sleep(1.5)
    await message.answer_photo(
        joke_file_2, 
        caption='I have caught you. HA!'
    )

