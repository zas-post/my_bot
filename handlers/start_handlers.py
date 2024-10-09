from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from database.database import (
    add_user,
)  # Импортируем функцию для добавления пользователя

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    # Получаем имя пользователя или задаем "пользователь", если имя не указано
    username = message.from_user.username or "пользователь"
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""

    # Добавляем пользователя в базу данных (параметр is_admin можно оставить False по умолчанию)
    add_user(
        user_id=message.from_user.id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        is_admin=False,  # По умолчанию все пользователи не являются администраторами
    )

    # Формируем текст ответа, используя словарь с текстами
    await message.answer(text=LEXICON_RU["start"].format(username=username))
