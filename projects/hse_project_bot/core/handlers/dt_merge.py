from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto


async def dt_merging_dataframes(message: Message, bot: Bot):
    comment_1 = "merge transactions & gender train by cliend_id"

    bf_1_1 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/merge/bf_1_1.jpg'
        )
    )

    bf_1_2 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/merge/bf_1_2.jpg'
        )
    )

    af_1 = FSInputFile(
        'core/handlers/media_files/data_transformations/merge/af_1.jpg'
    )

    code_1 = FSInputFile(
        'core/handlers/media_files/data_transformations/merge/code_1.jpg'
    )
    

    await message.answer(comment_1)
    await message.answer('Row dataframs:')
    await message.answer_media_group([bf_1_1, bf_1_2])
    await message.answer_photo(code_1, caption='code')
    await message.answer_photo(af_1, caption='result')

    