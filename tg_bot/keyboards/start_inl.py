from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

facts_numbers_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Факты просто число',
            callback_data='number_inl'
        )
    ],
    [
        InlineKeyboardButton(
            text='Факты по дню и месяцу',
            callback_data='day_month_inl'
        )
    ]
])