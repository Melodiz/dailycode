from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto


async def dt_data_cleaning(message: Message, bot: Bot):
    comment_1 = "Yes, it could have been simpler. "\
        "I was pursuing some other goal here. Here we can use .drop()"

    bf_1 = FSInputFile(
            'core/handlers/media_files/data_transformations/clean/1_bf.jpg'
        )

    af_1 = FSInputFile(
            'core/handlers/media_files/data_transformations/clean/1_af.jpg'
        )
    
    code_1 = FSInputFile(
            'core/handlers/media_files/data_transformations/clean/1.jpg'
        )
    



    await message.answer_photo(bf_1, caption='before')
    await message.answer_photo(code_1, caption='code')
    await message.answer_photo(af_1, caption='result')
    await message.answer(comment_1)
