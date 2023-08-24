from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME = State()
    GET_LAST_NAME = State()
    GET_AGE = State()

    GET_EXP_SUM = State()
    GET_EXP_CAT = State()
    GET_EXP_DESC = State()