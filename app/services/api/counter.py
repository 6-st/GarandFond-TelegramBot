from aiogram.fsm.context import FSMContext


async def update_counter(state: FSMContext, value: int) -> None:
    counter = await get_counter(state)
    await state.update_data(counter=counter + value)


async def get_counter(state: FSMContext) -> int:
    data = await state.get_data()
    return data["counter"]
