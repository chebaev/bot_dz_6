
import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from dotenv import load_dotenv

from  settings import BotSettings
from tg_bot.utils.commands import set_commands
from tg_bot.handlers.start import get_start
from tg_bot.handlers.history import get_history
from tg_bot.handlers.number import get_number, set_number
from tg_bot.handlers.day_month import get_day_month, set_day, set_month
from tg_bot.state.register import NumberState, DayMonthState



settings = BotSettings()
async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")



    bot = Bot(token=settings.token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher()

    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_history, Command(commands='history'))

    dp.callback_query.register(get_number, F.data.startswith('number_inl'))
    dp.message.register(set_number, NumberState.regNumber)

    dp.callback_query.register(get_day_month, F.data.startswith('day_month_inl'))
    dp.message.register(set_day, DayMonthState.regDay)
    dp.message.register(set_month, DayMonthState.regMonth)




    await set_commands(bot)

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())