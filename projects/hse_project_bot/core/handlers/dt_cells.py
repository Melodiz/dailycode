from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto


async def dt_edit_cells(message: Message, bot: Bot):
    comment_1 = "Let's make a histogram by bar chart. Yeah, "\
        "it's reinventing the wheel, but it's fun and more customizable."
    
    bf_1_row = FSInputFile(
        'core/handlers/media_files/data_transformations/cells/bf_1.jpg'
    )
    bf_1_plot = FSInputFile(
        'core/handlers/media_files/data_transformations/cells/bf_1_plot.png'
    )

    await message.answer(comment_1)
    await message.answer_photo(bf_1_row, caption='gr_menspendings')
    await message.answer_photo(bf_1_plot, caption='auto histogram')


    code_1_1 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/cells/code_1_1.jpg'
        )
    )

    code_1_2 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/cells/code_1_2.jpg'
        )
    )

    await message.answer('code:')
    await message.answer_media_group([code_1_1, code_1_2])
    
    af_1_row = FSInputFile(
        'core/handlers/media_files/data_transformations/cells/af_1_row.jpg'
    )

    await message.answer_photo(af_1_row, caption='result')
    await message.answer('visually:')

    af_1_plot_1 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/cells/af_1_plot_1.png'
        )
    )
    af_1_plot_2 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/cells/af_1_plot_2.png'
        )
    )
    af_1_plot_3 = InputMediaPhoto(
        type = 'photo', 
        media=FSInputFile(
            'core/handlers/media_files/data_transformations/cells/af_1_plot_3.png'
        )
    )
    await message.answer_media_group([
        af_1_plot_1, af_1_plot_2, af_1_plot_3
    ])
    