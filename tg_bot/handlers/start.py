from aiogram import Bot
from aiogram.types import Message

from tg_bot.keyboards.start_inl import facts_numbers_inline


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Здравствуйте {message.from_user.first_name}!\n\n'
                                                 f'<b>Факты о числах</b>\n\n'
                                                 f'API для интересных фактов о числах. Содержит мелочи,\n'
                                                 f'математические сведения, дату и год о числах.\n',
                                                 reply_markup=facts_numbers_inline)