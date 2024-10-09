from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    # Отправляем текст помощи пользователю
    await message.answer(text=LEXICON_RU["help"])
