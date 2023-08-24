from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from core.utils.dbconnect import Request


async def add_expenses(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name} введите сумму расхода:')
    await state.set_state(StepsForm.GET_EXP_SUM)


async def add_exp_sum(message: Message, state: FSMContext):
    await message.answer(f'Ваш расход: {message.text}\r\nТеперь выберите категорию расхода')
    await state.update_data(exponse=message.text)
    await state.set_state(StepsForm.GET_EXP_CAT)


async def add_exp_cat(message: Message, state: FSMContext):
    await message.answer(f"Выбрана категория {message.text}.\r\nЕсли необходимо введите описание траты:")
    await state.update_data(category=message.text)
    await state.set_state(StepsForm.GET_EXP_DESC)


async def add_exp_desc(message: Message, state: FSMContext, request: Request):
    await message.answer(f'Расход записан')
    await state.update_data(description=message.text)
    context_data = await state.get_data()
    summa = context_data.get('exponse')
    category = 2
    #category = context_data.get('category')
    desc = context_data.get('description')
    new_balance = await request.add_expense(message.from_user.id, summa, category, desc)
    await message.answer(f'Новый баланс: {new_balance}')
    await state.clear()

    

async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем заполнять анкету. Введи свое имя')
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Твоё имя: \r\n{message.text}\r\nТеперь введи фамилию.')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f'Твоя фамилия: \r\n{message.text}\r\nтеперь введи возраст')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, state: FSMContext):
    await message.answer(f'Твой возраст \r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Сохраненные данные в машине состояний: \r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = (f'Вот твои данные\r\n'
                 f'Имя: {name}\r\n'
                 f'Фамилия: {last_name}\r\n'
                 f'Возраст: {message.text}\r\n')
    await message.answer(data_user)
    await state.clear()