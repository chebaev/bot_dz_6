from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.core import crud
from site_API.core import site_api, url, headers, params
from site_API.core_trans import get_translator
from database.common.models import db, History
from tg_bot.state.register import NumberState

fact_by_number = site_api.get_math_fact()
db_write = crud.create()

async def get_number(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, f'Введите любое число от 0')
    await state.set_state(NumberState.regNumber)

async def set_number(message: Message, state: FSMContext):
    _number = message.text
    if _number.isdigit():

        await state.update_data(numbers=_number)
        response_number = fact_by_number("GET", url, headers, params, _number, 5)
        response_number = response_number.json()

        data = [{'number': response_number.get("number"), "message": response_number.get('text')}]
        db_write(db, History, data)
        text_number = response_number.get('text')

        await message.answer(f'Вы ввели число: {_number}\n'
                             f'{text_number}\n'
                             f'Перевод на русский:\n'
                             f'{(get_translator(text_number)).get('data').get('translatedText')}')
        await state.clear()
    else:
        await message.answer(f'Вы указали не число')

