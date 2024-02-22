from aiogram import Bot
from aiogram.types import Message


from database.core import crud
from database.common.models import db, History

db_print = crud.last_ten()

async def get_history(message: Message, bot: Bot):
    text = ''
    retrived = db_print(db, History, History.number, History.message)
    for element in retrived:
        text += f'{element.number} - {element.message}\n'
    await bot.send_message(message.from_user.id, text)