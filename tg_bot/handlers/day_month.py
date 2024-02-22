from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.core import crud
from site_API.core import site_api, url, headers, params
from site_API.core_trans import get_translator
from database.common.models import db, History
from tg_bot.state.register import DayMonthState

fact_by_date = site_api.get_date_fact()
db_write = crud.create()

async def get_day_month(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, f'Введите любую дату')
    await state.set_state(DayMonthState.regDay)

async def set_day(message: Message, state: FSMContext):
    _day = message.text
    if _day.isdigit():
        if 0 < int(_day) < 32:
            await state.update_data(day=_day)
            await message.answer(f'Вы ввели дату: {_day}\n')

            await message.answer(f'Укажите месяц цифрами\n')
            await state.set_state(DayMonthState.regMonth)
        else:
            await message.answer(f'Вы указали не верную дату')

    else:
        await message.answer(f'Вы указали не число')

async def set_month(message: Message, state: FSMContext):
    _month = message.text
    if _month.isdigit():
        if 0 < int(_month) < 13:
            await state.update_data(month=_month)
            reg_data = await state.get_data()
            reg_day = reg_data.get('day')
            reg_month = reg_data.get('month')
            await message.answer(f'Вы ввели день: {reg_day} месяц: {reg_month}\n')

            response_day = fact_by_date("GET", url, headers, params, reg_month, reg_day, 5)
            response_day = response_day.json()
            data = [{'number': response_day.get("year"), "message": response_day.get('text')}]
            db_write(db, History, data)
            text_day = response_day.get('text')
            await message.answer(f'Вы ввели день: {reg_day} месяц: {reg_month}\n'
                                 f'{text_day}\n'
                                 f'Перевод на русский:\n'
                                 f'{(get_translator(text_day)).get('data').get('translatedText')}')
            await state.clear()



        else:
            await message.answer(f'Токого месяца не бывает')
    else:
        await message.answer(f'Вы указали не число')


