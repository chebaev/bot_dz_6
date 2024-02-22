from aiogram.fsm.state import StatesGroup, State

class NumberState(StatesGroup):
    regNumber = State()

class DayMonthState(StatesGroup):
    regDay = State()
    regMonth = State()