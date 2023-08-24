from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services.api.counter import get_counter


class CounterCB(CallbackData, prefix="counter"):
    value: int


def get_counter_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="-1", callback_data=CounterCB(value=-1).pack())
    )
    builder.add(
        InlineKeyboardButton(text="+1", callback_data=CounterCB(value=1).pack())
    )

    return builder.as_markup()


async def send_counter_message(func, state: FSMContext):
    counter = await get_counter(state)
    await func(f"MeggaWhatt. Counter: {counter}", reply_markup=get_counter_keyboard())
