from aiogram.dispatcher.filters.state import State, StatesGroup


class Wiki_states(StatesGroup):
    w_theme = State()  # topilgan mavzu bo'yicha malumot olish uchun
