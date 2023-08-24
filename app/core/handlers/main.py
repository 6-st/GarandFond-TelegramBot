from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.core.keyboards.counter import (
    CounterCB,
    send_counter_message,
)
from app.services.api.counter import update_counter


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """/start command handling."""
    await state.update_data(counter=0)
    await send_counter_message(message.answer, state)


@router.callback_query(CounterCB.filter())
async def cb_counter(cb: CallbackQuery, callback_data: CounterCB, state: FSMContext):
    """Callback handler for increasing/decreasing counter"""
    await cb.answer()
    await update_counter(state, callback_data.value)
    await send_counter_message(cb.message.edit_text, state)  # type: ignore
