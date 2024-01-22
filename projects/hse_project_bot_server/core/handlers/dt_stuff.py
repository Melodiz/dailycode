from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto


async def dt_enother_stuff(message: Message, bot: Bot):
    comment_1 = "To find out for how many days (in days) users "\
        "made transactions, we need to go through all the transactions, "\
        "sorted by the user's ID and transaction time, count the day "\
        "of his first transaction and subtract it from the day of "\
        "the last transaction, make a dictionary out of it and turn it into a dataframe."
    
    bf_1 = FSInputFile(
            'core/handlers/media_files/data_transformations/enother/bf_1.jpg'
        )
    
    af_1 = FSInputFile(
            'core/handlers/media_files/data_transformations/enother/af_1_row.jpg'
        )
    
    code_1 = FSInputFile(
            'core/handlers/media_files/data_transformations/enother/code_1.jpg'
        )
    
    plot_1_1 = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/enother/plot_1_1.png'
        )
    )
    plot_1_2 = InputMediaPhoto(
        type='photo', 
        media=FSInputFile(
           'core/handlers/media_files/data_transformations/enother/plot_1_2.png' 
        )
    )

    await message.answer(comment_1)
    await message.answer_photo(bf_1, caption='row dataframe')
    await message.answer_photo(code_1, caption='code')
    await message.answer_photo(af_1, caption='result')
    await message.answer('visually:')
    await message.answer_media_group([plot_1_1, plot_1_2])